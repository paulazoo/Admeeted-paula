# Python standard libraries
from concurrent.futures import ThreadPoolExecutor
import time, json, os
from datetime import datetime

# Third-party libraries
from flask import Flask, jsonify, render_template, request, g, current_app, redirect, url_for, session
from flask_cors import CORS
from werkzeug import exceptions as wex
from flask.cli import with_appcontext
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

#firebase
import pyrebase

#socketio
from flask_socketio import SocketIO, emit, join_room, leave_room

# Internal imports
from db import init_db_command, get_db
from user import User
from main_db import main_convos, empty_hangouts
from chat_db import new_msg_db, get_msgs_db

'''
Paula and Samantha combined version!
'''

#%%
#for google auth
# Google Auth Configuration
"""
Storing the Google Client ID and Client Secret 
(from https://console.developers.google.com/  Credentials for this project)
App gets client credentials by reading environmental variables
"""
# GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_ID = "785353783740-5adk64k2huua2ftk2v2a9dp167qfk4iu.apps.googleusercontent.com"
# GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_CLIENT_SECRET = "Bks4vh98L-zEty2c3jsLXhZn"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

import os 
os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'

#%%
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
#socketio server
socket = SocketIO(app)
#cors = CORS(app, supports_credentials=True, resources={r"/*": {"origins": "https://www.admeeted.com"}})
cors = CORS(app)

#%%
# Bill's placeholder
loggedIn = False


# Bill's placeholder
@app.route('/me', methods=['GET'])
def me():
    '''
    Inputs: None
    Outputs: Whether user is currently logged in (Boolean)
    '''
    # placeholder code
    return jsonify(message=current_user.is_authenticated), 200

#%%
#google auth

#Note: can create another environment variable SECRET_KEY that Flask 
#and Flask-Login will use to cryptographically sign cookies and other items.


# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# Naive database setup
try:
    init_db_command()
except: 
    #og error: sqlite3.OperationalError:
    #TODO safe to assume firebase created?
    # Assume it's already been created
    pass

# OAuth 2 client setup
"""
Note: already using the Client ID from Google to initialize 
the oauthlib client in the WebApplicationClient.
"""
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



#Four endpoints for web application:
    
    #Homepage (Google Login btn redirect to Login endpoint):
@app.route("/")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.avatar
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'
    
    
    
    #Login (redirect to Google’s OAuth 2 Authorization endpoint):
        #(through OAuth 2 flow)
    
#Retrieve Google's provider configuration
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()
    #TODO: add error handling to the Google API call, just in case Google’s API 
    #returns a failure and not the valid provider configuration document.

    
@app.route("/login", methods=['POST'])
def login():
    profile = request.get_json(force=True)['profile']
    unique_id = profile['googleId']
    users_email = profile['email']
    picture = profile['imageUrl']
    users_name = profile['name']

    current_app.user_uid = unique_id
    session['user_uid'] = unique_id

    # Create a user in your db with the information provided
    # by Google
    user = User(
        id_=unique_id, name=users_name, email=users_email, avatar=picture
    )

    new_user = False # Remember to change back!

    # Doesn't exist? Add it to the database.
    if not User.get(unique_id):
        new_user=True
        print("User doesn't exist, creating new User")
        User.create(unique_id, users_name, users_email, picture)

    # Begin user session by logging the user in (using Flask Log-in)
    login_user(user)

    return jsonify(message=current_user.is_authenticated, new_user=new_user), 200


    #Logout Endpoint (logout and redirect back to homepage)

@app.route("/logout")
@login_required
#Note: ^this decorator from the Flask-Login toolbox and will make sure that 
#only logged in users can access this function (endpoint in this case).
def logout():
    logout_user()
    del session['user_uid']
    return jsonify(message=current_user.is_authenticated), 200


#%%
@app.route('/profile', methods=['GET','POST'])
def profile():
    #user_uid = ...?
    user_uid=session.get('user_uid')
    db=get_db()
    #if the profile form is edited and submitted
    if request.method == 'POST':
        try:
            pdata = request.get_json(force=True)['new_data']
            print(f"Request data: {pdata}")
            db.child('users').child(user_uid).update({
                    'displayName':pdata['displayName'],
                    'state':pdata['state'],
                    'country':pdata['country'],
                    })
            
            majors=pdata['majors']
            prev_majors = db.child('major_user').child(user_uid).get().val()

            majors_dict = dict.fromkeys(majors, True)
            db.child('major_user').child(user_uid).set(majors_dict)
            if prev_majors:
                prev_majors = list(prev_majors)
            else:
                prev_majors = []

            new_majors = set(majors) - set(prev_majors)
            old_majors = set(prev_majors) - set(majors)

            for major in new_majors:
                db.child('user_major').child(major).set({user_uid: True})
            for major in old_majors:
                db.child('user_major').child(major).set({user_uid: None})

            interests=pdata['interests']
            prev_interests = db.child('interest_user').child(user_uid).get().val()

            interests_dict = dict.fromkeys(interests, True)
            db.child('interest_user').child(user_uid).set(interests_dict)
            if prev_interests:
                prev_interests = list(prev_interests)
            else:
                prev_interests = []

            print(f'Interests: {interests}')
            print(f'Prev Interests: {prev_interests}')

            new_interests = set(interests) - set(prev_interests)
            old_interests = set(prev_interests) - set(interests)

            print(f'New Interests: {new_interests}')
            print(f'Old Interests: {old_interests}')

            for interest in new_interests:
                db.child('user_interest').child(interest).set({user_uid: True})
            for interest in old_interests:
                db.child('user_interest').child(interest).set({user_uid: None})

            return jsonify(message=True), 200
        except Exception as e:
            print(e)
            return jsonify(message=False), 400
    
    #get profile data
    user=db.child('users').child(user_uid).get().val()

    majors = db.child('major_user').child(user_uid).get().val()
    majors_keys=[]
    
    if majors:
        majors_keys = list(majors.keys())

    interests = db.child('interest_user').child(user_uid).get().val()
    interests_keys = []

    if interests:
        interests_keys = list(interests.keys())
    
    data={
        'name':user['name'],
        'displayName':user.get('displayName', user['name']),
        'state':user.get('state'),
        'country':user.get('country'),
        'avatar':user['avatar'],
        'majors':majors_keys,
        'interests': interests_keys
     }
    
    return jsonify(message=data), 200

@app.route('/upcoming-events', methods=['GET'])
def upcoming_events():
    db=get_db()
    user_uid=session.get('user_uid')
    events=db.child('event_user').child(user_uid).get().val()

    data=[]
    if events:
        for event in events:
            event_info_ord=db.child('events').child(event).get().val()
            event_timeEnd=datetime.strptime(event_info_ord['timeEnd'], '%H:%M %d %B %Y')

            if event_timeEnd>=datetime.now():
                event_info=dict(event_info_ord)
                event_info.update({'id':event})

                org_info = db.child('orgs').child(event_info['org']).get().val()
                event_info.update({'avatar': org_info['avatar']})

                convos_data = get_convo_event(db, user_uid, event)
                event_info.update({'convos': convos_data})

                data.append(event_info)

    return jsonify(message=data), 200

def get_convo_event(db, user_uid, event_uid):
    '''
    Helper method for upcoming_events() and upcoming_events_org()
    '''
    event_convos_ord = db.child('convo_event').child(event_uid).get().val()
    user_convos_ord = db.child('convo_user').child(user_uid).get().val()

    convos_data = []
    if event_convos_ord and user_convos_ord:
        convos = set(event_convos_ord) & set(user_convos_ord)

        for convo in convos:
            convo_info = db.child('convos').child(convo).get().val()

            convos_data.append({
                'displayName': convo_info['displayName'],
                'timeStart': convo_info['timeStart'],
                'link': convo_info.get('link', '')
            })

    return convos_data

@app.route('/upcoming-events/<org_uid>', methods=['GET'])
def upcoming_events_org(org_uid):
    db=get_db()
    user_uid=session.get('user_uid')
    events_users=db.child('event_user').child(user_uid).get().val()
    events_orgs=db.child('event_org').child(org_uid).get().val()

    data = []
    if events_users and events_orgs:
        events=set(events_users) & set(events_orgs)

        for event in events:
            event_info_ord=db.child('events').child(event).get().val()
            event_timeEnd=datetime.strptime(event_info_ord['timeEnd'], '%H:%M %d %B %Y')
        
            if event_timeEnd>=datetime.now():
                event_info=dict(event_info_ord)
                event_info.update({'id':event})

                convos_data = get_convo_event(db, user_uid, event)
                event_info.update({'convos': convos_data})
                data.append(event_info)

            
    return jsonify(message=data), 200


@app.route('/avail-events', methods=['GET'])
def avail_events():
    start = time.time()
    db=get_db()
    user_uid=session.get('user_uid')
    orgs=db.child('org_user').child(user_uid).get().val()
    print(f"Get Orgs Time: {time.time() - start}")

    def _grab_events(all_events, db, org):
        start = time.time()
        org_events = db.child('event_org').child(org).get().val()
        if org_events:
            all_events.update(dict(org_events))
        print(f'Thread Event Time: {time.time() - start}')

    def _grab_events_info(data, db, event):
        start = time.time()
        event_info_ord = db.child('events').child(event).get().val()
        event_timeDeadline = datetime.strptime(event_info_ord['timeDeadline'], '%H:%M %d %B %Y')

        if event_timeDeadline >= datetime.now():
            event_info = dict(event_info_ord)
            event_info.update({'id': event})

            avatar = db.child('orgs').child(event_info['org']).child('avatar').get().val()
            event_info.update({'avatar': avatar})

            data.append(event_info)

        print(f'Thread Info Time: {time.time() - start}')

    data = []
    if orgs:
        all_events={}
        with ThreadPoolExecutor() as executor:
            for org in orgs:
                executor.submit(_grab_events, all_events, db, org)

        print(f"Get Events Time: {time.time() - start}")

        events_users=db.child('event_user').child(user_uid).get().val()

        if not events_users:
            events_users = {}

        events=set(all_events) - set(events_users)

        with ThreadPoolExecutor() as executor:
            for event in events:
                executor.submit(_grab_events_info, data, db, event)

    print(f"Total Events Time: {time.time() - start}")
            
    return jsonify(message=data), 200

@app.route('/avail-events/<org_uid>', methods=['GET'])
def avail_events_org(org_uid):
    db=get_db()
    user_uid=session.get('user_uid')
    events_users=db.child('event_user').child(user_uid).get().val()
    events_orgs=db.child('event_org').child(org_uid).get().val()

    data = []
    if events_orgs:
        if not events_users:
            events_users = {}

        events=set(events_orgs) - set(events_users)

        for event in events:
            event_info_ord=db.child('events').child(event).get().val()
            event_timeDeadline=datetime.strptime(event_info_ord['timeDeadline'], '%H:%M %d %B %Y')
        
            if event_timeDeadline>=datetime.now():
                event_info=dict(event_info_ord)
                event_info.update({'id':event})

                data.append(event_info)
            
    return jsonify(message=data), 200

@app.route('/events/<event_uid>', methods=['GET', 'POST'])
def events(event_uid):
    db=get_db()
    user_uid=session.get('user_uid')
    
    if request.method == 'POST':
        signup_cancel = request.get_json(force=True)['new_data'] #...sign up vs cancel?
        print(f'Signup Cancel: {signup_cancel}')
        try:
            event = db.child('events').child(event_uid).get().val()
            event_timeDeadline = datetime.strptime(event['timeDeadline'], '%H:%M %d %B %Y')
            if event_timeDeadline >= datetime.now(): # If deadline has not passed
                if signup_cancel==True: # User wants to sign up
                    db.child('event_user').child(user_uid).update({event_uid:True})
                    db.child('user_event').child(event_uid).update({user_uid:True})
                elif signup_cancel==False: # User wants to cancel
                    db.child('event_user').child(user_uid).update({event_uid: None})
                    db.child('user_event').child(event_uid).update({user_uid: None})
                return jsonify(message=True), 200
            else:
                return jsonify(message=False), 400

        except Exception as e:
            print(e)
            return jsonify(message=False), 400
    
    data=dict(db.child('events').child(event_uid).get().val())
    data.update({'event_uid':event_uid})
    return jsonify(message=data), 200

@app.route('/past-conversations', methods=['GET'])
def past_convos():
    start = time.time()
    db=get_db()
    user_uid=session.get('user_uid')
    convos=db.child('convo_user').child(user_uid).get().val()

    def _grab_convo(data, db, convo):
        start = time.time()
        convo_info = db.child('convos').child(convo).get().val()
        convo_timeEnd = datetime.strptime(convo_info['timeEnd'], '%H:%M %d %B %Y')

        if convo_timeEnd <= datetime.now():  # Only conversations that have ended
            convo_info.update({'id': convo})

            avatar = db.child('orgs').child(convo_info['org']).child('avatar').get().val()
            convo_info.update({'avatar': avatar})
            data.append(convo_info)

    data = []
    if convos:
        with ThreadPoolExecutor() as executor:
            for convo in convos:
                executor.submit(_grab_convo, data, db, convo)

    return jsonify(message=data), 200


@app.route('/past-conversations/<org_uid>', methods=['GET'])
def past_convos_org(org_uid):
    db = get_db()
    user_uid = session.get('user_uid')

    convos = db.child('convo_user').child(user_uid).get().val()

    data = []
    if convos:
        for convo in convos:
            convo_info = db.child('convos').child(convo).get().val()
            convo_timeEnd = datetime.strptime(convo_info['timeEnd'], '%H:%M %d %B %Y')
            # Only conversations that have ended and are part of this organization
            if convo_timeEnd <= datetime.now() and convo_info['org'] == org_uid:
                convo_info.update({'id': convo})
                data.append(convo_info)

    return jsonify(message=data), 200

@app.route('/generate-convos/<event_uid>', methods=['POST'])
def generate_convos(event_uid):
    print("I HAVE ARRIVED")
    if request.method == 'POST':
        try:
            gen_convo_inputs= request.get_json(force=True)
            print(f'Inputs: {gen_convo_inputs}')
            num_threads = gen_convo_inputs.get('num_threads', 4)
            main_convos(event_uid, gen_convo_inputs['convo_name'], num_threads)
            return jsonify(message=True), 200
        except Exception as e:
            print(e)
            return jsonify(message=False), 400

@app.route('/all-organizations', methods=['GET'])
def all_orgs():
    db=get_db()
    orgs=db.child('orgs').get().val()

    data = []
    for org in orgs:
        org_info = orgs[org]
        org_info.update({'id': org})
        data.append(org_info)

    return jsonify(message=data), 200

@app.route('/organizations/<org_uid>', methods=['GET', 'POST'])
def other_orgs(org_uid):
    db=get_db()
    user_uid=session.get('user_uid')
    if request.method == 'POST':
        # code=str(db.child('orgs').child(org_uid).get().val())
        signup_cancel = request.get_json(force=True)['new_data']
        # signup_cancel = request.get_json(force=True)['new_data'][0]
        # input_code=request.get_json(force=True)['new_data'][1]
        try:    
            if signup_cancel==True:
                # if input_code==code:
                    db.child('org_user').child(user_uid).update({org_uid:True})
                    db.child('user_org').child(org_uid).update({user_uid:True})
            elif signup_cancel==False:
                db.child('org_user').child(user_uid).update({org_uid: None})
                db.child('user_org').child(org_uid).update({user_uid: None})
            return jsonify(message=True), 200
        except Exception as e:
            print(e)
            return jsonify(message=False), 400

    data=dict(db.child('orgs').child(org_uid).get().val())
    if data:
        #admin...? Need to edit database later
        data.update({'id':org_uid, 'admin':False})
        org_users=db.child('user_org').child(org_uid).shallow().get().val()
        if org_users and str(user_uid) in org_users:
            data.update({'joined':True})
    
    elif not data:
        data = {}
    return jsonify(message=data), 200

@app.route('/organizations', methods=['GET'])
def organizations():
    '''
    Inputs: user_uid
    Outputs: a list containing the info (in dicts) for all of a user's organizations
    '''
    start = time.time()
    db=get_db()

    user_uid=session.get('user_uid')
    user_orgs = db.child('org_user').child(user_uid).get().val()

    def _grab_orgs(data, db, org):
        start = time.time()
        dictionary = dict(db.child('orgs').child(org).get().val())
        dictionary['id'] = org
        data.append(dictionary)

    data = []  # list of dictionaries containing info for each of a user's orgs
    if user_orgs:
        with ThreadPoolExecutor() as executor:
            for org in user_orgs:
                executor.submit(_grab_orgs, data, db, org)

    return jsonify(message=data), 200


@app.route('/create-hangouts', methods=['POST'])
def create_empty_hangouts():
    if request.method == 'POST':
        gen_hangouts_inputs = request.get_json(force=True)
        print(gen_hangouts_inputs)
        num_threads = gen_hangouts_inputs.get('num_threads', 4)
        name = gen_hangouts_inputs.get('name', 'Hangout')
        try:
            empty_hangouts(name, gen_hangouts_inputs['num_hangouts'], num_threads)
            return jsonify(message=True), 200
        except Exception as e:
            print(e)
            return jsonify(message=False), 400


@app.route('/majors', methods=['GET'])
def majors():
    db = get_db()
    data = db.child('majors').get().val()
    if data:
        data = list(data)
    else:
        data = []

    return jsonify(message=data), 200


@app.route('/interests', methods=['GET'])
def interests():
    db = get_db()
    data = db.child('interests').get().val()
    if data:
        data = list(data)
    else:
        data = []

    return jsonify(message=data), 200


#%%
#socketio server stuff
@socket.on('connect')
def connect_message():
    print("socket connect api!")

@socket.on('join')
def on_join(convo_uid):
    join_room(convo_uid)
    user_uid=session.get("user_uid")
    db=get_db()
    db.child("convo_actuser").child(convo_uid).update({user_uid:True})
    actusers=db.child("convo_actuser").child(convo_uid).get().val()
    displayNames=[]
    for user in actusers:
        displayNames.append({db.child("users").child(user).child("displayName").get().val()})
    emit("userjoined", displayNames, room=convo_uid, broadcast=True, namespace="/")
    print(actusers, displayNames)

@socket.on('leave')
def on_leave(convo_uid):
    leave_room(convo_uid)

@socket.on('sendmsg')
def custom_ok_message(msg, convo_uid):
    user_uid=session.get('user_uid')
    print(" sent msg to api!")
    #print('sendmsg api got it!!!'+str(msg))
    if msg:
        new_msg_db(user_uid, msg, convo_uid)
    msgs_data=get_msgs_db(convo_uid)
    emit("recmsg", msgs_data, room=convo_uid, broadcast=True, namespace="/")

@app.route('/convochat/<convo_uid>', methods=['GET'])
def convochat_init(convo_uid):
    #...bc user can't change convos?
    db=get_db()
    user_uid=session.get('user_uid')
    convoDisplayName=db.child("convos").child(convo_uid).child("displayName").get().val()
    
    convo_user = db.child("convo_user").child(user_uid).child(convo_uid).get().val()

    #print(convo_user)
    if convo_user:
        userInConvo=True
        videolink=db.child("convos").child(convo_uid).child("link").get().val()
    else:
        userInConvo=False
        videolink=""

    return jsonify(userInConvo=userInConvo, convoDisplayName=convoDisplayName, videolink=videolink), 200

#%%
#To run your Flask application on your local computer to test the login flow
if __name__ == "__main__":
    #app.run(ssl_context="adhoc")
    print("running")
    socket.run(app, debug = True)











#%%
# -------------------------------------------------------------
# Bill's placeholders
upcoming_convos_old_data = {
    1: [{
        'id': 0,
        'displayName': 'Coca-Cola Scholars 2020',
        'org': 1,
        'timeStart': time.time(),
        'timeEnd': time.time()
    }],
    0: [{
        'id': 1,
        'displayName': 'Virtual Visitas',
        'org': 0,
        'timeStart': time.time(),
        'timeEnd': time.time()
    }],
    2: []
}

@app.route('/upcoming-convos/<int:org_uid>')
def upcoming_convos_org(org_uid):
    return jsonify(message=upcoming_convos_old_data[org_uid]), 200

@app.route('/upcoming-convos')
def upcoming_convos():
    return jsonify(message=
        [
            {
                'id': 0,
                'displayName': 'Coca-Cola Scholars 2020',
                'org': 1,
                'timeStart': time.time(),
                'timeEnd': time.time()
            },
            {
                'id': 1,
                'displayName': 'Virtual Visitas',
                'org': 0,
                'timeStart': time.time(),
                'timeEnd': time.time()
            }
        ]
    ), 200

past_convos_old_data = {
    0: [{
       'id': 2,
       'displayName': 'Paula, Bill, Samantha',
       'org': 0,
       'timeStart': time.time(),
       'timeEnd': time.time(),
       'link': 'https://hangouts.google.com/group/u5Dg6H94cGFjg9JaA'
   },
   {
       'id': 3,
       'displayName': 'Bill, Samantha, Paula',
       'org': 0,
       'timeStart': time.time(),
       'timeEnd': time.time(),
       'link': 'https://hangouts.google.com/group/u5Dg6H94cGFjg9JaA'
   }],
    1: [],
    2: []
}

@app.route('/past-convos/<int:org_uid>')
def past_convos_org_old(org_uid):
    return jsonify(message=past_convos_old_data[org_uid]), 200

@app.route('/past-convos', methods=['GET'])
def past_convos_old():
    return jsonify(message=
                   [
                       {
                           'id': 2,
                           'displayName': 'Paula, Bill, Samantha',
                           'org': 0,
                           'timeStart': time.time(),
                           'timeEnd': time.time(),
                           'link': 'https://hangouts.google.com/group/u5Dg6H94cGFjg9JaA'
                       },
                       {
                           'id': 3,
                           'displayName': 'Bill, Samantha, Paula',
                           'org': 0,
                           'timeStart': time.time(),
                           'timeEnd': time.time(),
                           'link': 'https://hangouts.google.com/group/u5Dg6H94cGFjg9JaA'
                       },
                   ]), 200

avail_convos_old_data = {
    2: [{
       'id': 4,
       'displayName': 'Tennis Social #1',
       'org': 2,
       'timeStart': time.time(),
       'timeEnd': time.time()
    },
    {
       'id': 5,
       'displayName': 'Tennis Social #2',
       'org': 2,
       'timeStart': time.time(),
       'timeEnd': time.time()
    }],
    1: [],
    0: [{
       'id': 6,
       'displayName': 'First-Year Orientation',
       'org': 0,
       'timeStart': time.time(),
       'timeEnd': time.time()
    }]
}

@app.route('/convos-old/<int:convo_id>', methods=['POST'])
def convos_old(convo_id):
    signUp = request.get_json(force=True)['new_data']
    print(signUp)
    return jsonify(message=True), 200


@app.route('/avail-convos/<int:org_uid>')
def avail_convos_org(org_uid):
    return jsonify(message=avail_convos_old_data[org_uid]), 200

@app.route('/avail-convos', methods=['GET'])
def avail_convos():
    return jsonify(message=
                   [
                       {
                           'id': 4,
                           'displayName': 'Tennis Social #1',
                           'org': 2,
                           'timeStart': time.time(),
                           'timeEnd': time.time()
                       },{
                           'id': 6,
                           'displayName': 'First-Year Orientation',
                           'org': 0,
                           'timeStart': time.time(),
                           'timeEnd': time.time()
                       },
                       {
                           'id': 5,
                           'displayName': 'Tennis Social #2',
                           'org': 2,
                           'timeStart': time.time(),
                           'timeEnd': time.time()
                       }
                   ]), 200

organizations_old_data = {
    0: {
        'displayName': 'Harvard Class of 2024',
        'dateFounded': time.time(),
        'description': 'Group for connecting Harvard pre-first year students!',
        'avatar': '/logo192.png',
        'joined': True,
        'admin': True
    },
    1: {
        'displayName': 'Coca-Cola Scholars',
        'dateFounded': time.time(),
        'description': 'Group for connecting Coca-Cola Scholars!',
        'avatar': '/logo192.png',
        'joined': True,
        'admin': False
    },
    2: {
        'displayName': 'Tennis Academy of the South',
        'dateFounded': time.time(),
        'description': 'Group for connecting young and aspiring tennis players!',
        'avatar': '/logo192.png',
        'joined': False,
        'admin': False
    }
}

@app.route('/organizations-old/<int:org_uid>', methods=['GET', 'POST'])
def organization_old(org_uid):
    global organizations_old_data
    if request.method == 'POST':
        organizations_old_data[org_uid]['joined'] = not organizations_old_data[org_uid]['joined']
        return jsonify(message=organizations_old_data[org_uid]['joined']), 200
    return jsonify(message=organizations_old_data[org_uid]), 200

@app.route('/organizations-old', methods=['GET'])
def organizations_old():
    return jsonify(message=
                   [
                       {
                           'id': 0,
                           'displayName': 'Harvard Class of 2024',
                           'timeStart': time.time(), # This is placeholder
                       },
                       {
                           'id': 1,
                           'displayName': 'Coca-Cola Scholars',
                           'timeStart': time.time(),  # This is placeholder
                       }
                   ])

@app.route('/all-organizations-old', methods=['GET'])
def all_organizations_old():
    return jsonify(message=
                   [
                       {
                           'id': 0,
                           'displayName': 'Harvard Class of 2024'
                       },
                       {
                           'id': 1,
                           'displayName': 'Coca-Cola Scholars'
                       },
                       {
                           'id': 2,
                           'displayName': 'Tennis Academy of the South'
                       }
                   ])

profile_old_data = {
    'name': '<Google Profile Name>',
    'displayName': 'Albert Zhang',
    'state': 'Georgia',
    'country': 'USA',
    'avatar': '<Google Profile Picture>',
    'interests': [
        'cooking',
        'coding'
    ]
}

@app.route('/profile-old', methods=['GET', 'POST'])
def profile_old():

    return jsonify(message=
                   {
                       'email': 'albertzhang9000@gmail.com',
                       'displayName': 'Albert Zhang',
                       'state': 'Georgia',
                       'country': 'USA',
                      #TODO: need participating : true back?
                       'avatar': ''
                   }
    ), 200


# -------------------------------------------------------------
# Samantha's placeholders
    
#%%
# @app.route('/organizations', methods=['GET'])
# def organizations():
#     '''
#     Inputs: user_uid
#     Outputs: a list containing the info (in dicts) for all of a user's organizations
#     '''
#     org_info_list = [] #list of dictionaries containg info for each of a user's orgs
#     user_uid=g.user_uid
#     user_orgs = dict(get_db().child('org_user').child(user_uid).get().val())
#     for key in user_orgs:
#         #where key is an org
#         dictionary = dict(get_db().child('orgs').child(key).get().val())
#         dictionary['id'] = key
#         org_info_list.append(dictionary)
        
    
#     return jsonify(message=org_info_list), 200
#%%


    global profile_old_data
    if request.method == 'POST':
        print(request.get_json(force=True))
        profile_old_data['displayName'] = request.get_json(force=True)['new_data']['displayName']
        profile_old_data['state'] = request.get_json(force=True)['new_data']['state']
        profile_old_data['country'] = request.get_json(force=True)['new_data']['country']
        profile_old_data['interests'] = request.get_json(force=True)['new_data']['interests']
        return jsonify(message=True), 200
    return jsonify(message=profile_old_data), 200


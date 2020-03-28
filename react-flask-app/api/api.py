# Python standard libraries
import time, json, os, datetime

# Third-party libraries
from flask import Flask, jsonify, render_template, request, g, current_app, redirect, url_for
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

# Internal imports
from db import init_db_command
from user import User
import db_for_flask

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

Windows users: set GOOGLE_CLIENT_ID=your_client_id in Command Prompt
"""
GOOGLE_CLIENT_ID = '667088492207-2fch6bc6r8b40fm40hjv8mq0n6minrr2.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'CFG-c2H48GDs_xdxvDj4nFAb'
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)


#%%
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

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
    return jsonify(isLoggedIn=loggedIn), 200

# Bill's placeholder
#@app.route('/login', methods=['POST'])
#def login():
#    '''
#    Inputs will be a username (String) and password (String)
#    Outputs will be whether user successfully logs in (Boolean)
#    '''
#    # Placeholder code
#    loggedIn = True
#    return jsonify(isLoggedIn=loggedIn), 200
#
## Bill's placeholder
#@app.route('/logout', methods=['GET'])
#def logout():
#    loggedIn = False
#    return jsonify(isLoggedIn=loggedIn), 200

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

    
@app.route("/login")
def login():
    print("login")
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
        #Note: openid is a required scope to tell Google to initiate the 
        #OIDC flow, which will authenticate the user by having them log in.
    )
    
    return redirect(request_uri)



    #Login Callback:
"""
This login endpoint is the jumping point for all of Google’s work 
authenticating the user and asking for consent. Once the user logs in with
Google and agrees to share their email and basic profile information
with this application, Google generates a unique code that it sends here.
"""

#Define login callback endpoint and get Google's code
@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

# Find out what URL (Google's token endpoint) to hit to get tokens that allow 
#you to ask for things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

# Prepare a request to get tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
        )
# Send a request to get tokens!
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
        )

# Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    
# Now that have tokens, find and hit the URL
# from Google that gives this app the user's profile information,
# including their Google profile image and email
    #checking the userinfo_endpoint field in the provider configuration document
    #for location of user info endpoint and its standardized URL
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    
    #use oauthlib to add the token to your request
    uri, headers, body = client.add_token(userinfo_endpoint)
    #use requests to send it out
    userinfo_response = requests.get(uri, headers=headers, data=body)

    
# You want to make sure their email is verified.
# The user authenticated with Google, authorized your
# app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400
    
# Create a user in your db with the information provided
# by Google
    user = User(
        id_=unique_id, name=users_name, email=users_email, avatar=picture
        )

# Doesn't exist? Add it to the database.
    if not User.get(unique_id):
        print("User doesn't exist, creating new User")
        User.create(unique_id, users_name, users_email, picture)

# Begin user session by logging the user in (using Flask Log-in)
    login_user(user)

# Send user back to homepage
    return redirect(url_for("index"))



    #Logout Endpoint (logout and redirect back to homepage)
@app.route("/logout")
@login_required
#Note: ^this decorator from the Flask-Login toolbox and will make sure that 
#only logged in users can access this function (endpoint in this case).
def logout():
    logout_user()
    return redirect(url_for("index"))


#%%
@app.route('/profile', methods=['GET','POST'])
def profile():
    #user_uid = ...?
    user_uid=g.user_uid
    #if the profile form is edited and submitted
    if request.method == 'POST':
        try:
            pdata = request.get_json()
            g.db.child('users').child(user_uid).update({
                    'displayName':pdata['displayName'],
                    'state':pdata['state'],
                    'country':pdata['country'],
                    })
            
            majors=pdata['major']
            majors_dict=dict.fromkeys(majors, True)
            
            g.db.child('major_user').child(user_uid).update(majors_dict)
            for major in majors:
                g.db.child('user_major').child(major).update({user_uid: True})

            return True, 200
        except:
            return False, 400
    
    #get profile data
    user=g.db.child('users').child(user_uid).get().val()
    
    majors=list(g.db.child('major_user').child(user_uid).get().val().keys())
    
    data={'name':user['name'], 
     'displayName':user['displayName'],
     'state':user['state'],
     'country':user['country'],
     'avatar':user['avatar'],
     'major':majors
     }
    
    return jsonify(message=data), 200
  
    
@app.route('/profile/<other_user_uid>', methods=['GET'])
def other_profile(other_user_uid):
    
    profile_data=db_for_flask.db_profile(other_user_uid)
    
    return jsonify(message=profile_data), 200

@app.route('/majors', methods=['GET'])
def majors():
    data=g.db.child('majors').get().val()
     
    return jsonify(message=data), 200


@app.route('/upcoming-events', methods=['GET'])
def upcoming_events():
    user_uid=g.user_uid
    events=g.db.child('event_user').child(user_uid).get().val()
    data=[]
    for event in events:
        event_info_ord=g.db.child('events').child(event).get().val()
        event_timeStart=datetime.strptime(event_info_ord['timeStart'], '%H:%M %d %B %Y')
    
        if event_timeStart<=datetime.now():
            event_info=dict(event_info_ord)
            event_info.update({'event_uid':event})
            data.append(event_info)
     
    return jsonify(message=data), 200

@app.route('/upcoming-events/<org_uid>', methods=['GET'])
def upcoming_events_org(org_uid):
    user_uid=g.user_uid
    events_users=g.db.child('event_user').child(user_uid).get().val()
    events_orgs=g.db.child('event_org').child(org_uid).get().val()
    events=set(events_users) & set(events_orgs)
    data=[]
    for event in events:
        event_info_ord=g.db.child('events').child(event).get().val()
        event_timeStart=datetime.strptime(event_info_ord['timeStart'], '%H:%M %d %B %Y')
    
        if event_timeStart<=datetime.now():
            event_info=dict(event_info_ord)
            event_info.update({'event_uid':event})
            data.append(event_info)   
            
    return jsonify(message=data), 200

@app.route('/avail-events', methods=['GET'])
def avail_events(org_uid):
    user_uid=g.user_uid
    orgs=g.db.child('org_user').child(user_uid).get().val()
    all_events={}
    for org in orgs:
        org_events=g.db.child('event_org').child(org).get().val()
        all_events.update(dict(org_events))
    events_users=g.db.child('event_user').child(user_uid).get().val()
    events=set(all_events) - set(events_users)
    data=[]
    for event in events:
        event_info_ord=g.db.child('events').child(event).get().val()
        event_timeStart=datetime.strptime(event_info_ord['timeStart'], '%H:%M %d %B %Y')
    
        if event_timeStart<=datetime.now():
            event_info=dict(event_info_ord)
            event_info.update({'event_uid':event})
            data.append(event_info)
            
    return jsonify(message=data), 200

@app.route('/avail-events/<org_uid>', methods=['GET'])
def avail_events_org(org_uid):
    user_uid=g.user_uid
    events_users=g.db.child('event_user').child(user_uid).get().val()
    events_orgs=g.db.child('event_org').child(org_uid).get().val()
    events=set(events_orgs) - set(events_users)
    data=[]
    for event in events:
        event_info_ord=g.db.child('events').child(event).get().val()
        event_timeStart=datetime.strptime(event_info_ord['timeStart'], '%H:%M %d %B %Y')
    
        if event_timeStart<=datetime.now():
            event_info=dict(event_info_ord)
            event_info.update({'event_uid':event})
            data.append(event_info)
            
    return jsonify(message=data), 200

@app.route('/events/<event_uid>', methods=['GET', 'POST'])
def events(event_uid):
    user_uid=g.user_uid
    
    if request.method == 'POST':
        signup_cancel = request.get_json() #...sign up vs cancel?
        try:
            if signup_cancel==True:
                g.db.child('event_user').child(user_uid).update({event_uid:True})
                g.db.child('user_event').child(event_uid).update({user_uid:True})
            elif signup_cancel==False:
                g.db.child('event_user').child(user_uid).update({event_uid: None})
                g.db.child('user_event').child(event_uid).update({user_uid: None})
            return True, 200
        except:
            return False, 400
    
    data=dict(g.db.child('events').child(event_uid).get().val())
    data.update({'event_uid':event_uid})
    return jsonify(message=data), 200

@app.route('/conversations', methods=['GET'])
def convos():
    user_uid=g.user_uid
    convos=g.db.child('convo_user').child(user_uid).get().val()
    data={}
    for convo in convos:
        convo_info=g.db.child('convos').child(convo).get().val()
        convo_info.update({'convo_uid': convo})
        data.update(convo_info)
    return jsonify(message=data), 200

@app.route('/all_organizations', methods=['GET'])
def all_orgs(other_user_uid):
    data=g.db.child('orgs').get().val()
     
    return jsonify(message=data), 200


@app.route('/organizations/<org_uid>', methods=['GET', 'POST'])
def other_orgs(org_uid):
    user_uid=g.user_uid
    if request.method == 'POST':
        signup_cancel, org_uid = request.get_json() #...sign up vs cancel?
        try:    
            if signup_cancel==True:
                g.db.child('org_user').child(user_uid).update({org_uid:True})
                g.db.child('user_org').child(org_uid).update({user_uid:True})
            elif signup_cancel==False:
                g.db.child('org_user').child(user_uid).update({org_uid: None})
                g.db.child('user_org').child(org_uid).update({user_uid: None})
            return True, 200
        except:
            return False, 400
    data=dict(g.db.child('orgs').child(org_uid).get().val())
    #admin...? Need to edit database later
    data.update({'org_uid':org_uid, 'admin':True})
    org_users=g.db.child('user_org').child(org_uid).shallow().get().val()
    if str(user_uid) in org_users:
        data.update({'joined':True})
        
    return jsonify(message=data), 200

@app.route('/organizations', methods=['GET'])
def organizations():
    '''
    Inputs: user_uid
    Outputs: a list containing the info (in dicts) for all of a user's organizations
    '''
    org_info_list = [] #list of dictionaries containg info for each of a user's orgs
    user_uid=g.user_uid
    user_orgs = dict(g.db.child('org_user').child(user_uid).get().val())
    for key in user_orgs:
        #where key is an org
        org_info_list.append(dict(g.db.child('orgs').child(key).get().val()))
        
    
    return jsonify(message=org_info_list), 200
#%%
@app.route('/conversations/<convo_uid>', methods=['GET'])
def other_convos(convo_uid):
    #...bc user can't change convos?
    user_uid=g.user_uid
    other_convos_data = db_for_flask.db_other_convos(user_uid, convo_uid)
    return jsonify(message=other_convos_data), 200


#%%
#To run your Flask application on your local computer to test the login flow
if __name__ == "__main__":
    app.run(ssl_context="adhoc")
    print("running")







#%%
# -------------------------------------------------------------
# Bill's placeholders
@app.route('/upcoming-convos')
def upcoming_convos():
    return jsonify(message=
        [
            {
                'id': 0,
                'name': 'Coca-Cola Scholars 2020',
                'displayName': 'Coca-Cola Scholars 2020',
                'time': time.time()
            },
            {
                'id': 1,
                'name': 'Virtual Visitas',
                'displayName': 'Virtual Visitas',
                'time': time.time()
            }
        ]
    ), 200

@app.route('/past-convos', methods=['GET'])
def past_convos():
    return jsonify(message=
                   [
                       {
                           'id': 2,
                           'name': 'Virtual Visitas Test 1',
                           'displayName': 'Paula, Bill, Samantha',
                           'time': time.time()
                       },
                       {
                           'id': 3,
                           'name': 'Virtual Visitas Test 2',
                           'displayName': 'Bill, Samantha, Paula',
                           'time': time.time()
                       },
                       {
                           'id': 2,
                           'name': 'Virtual Visitas Test 1',
                           'displayName': 'Paula, Bill, Samantha',
                           'time': time.time()
                       },
                       {
                           'id': 3,
                           'name': 'Virtual Visitas Test 2',
                           'displayName': 'Bill, Samantha, Paula',
                           'time': time.time()
                       }, {
                           'id': 2,
                           'name': 'Virtual Visitas Test 1',
                           'displayName': 'Paula, Bill, Samantha',
                           'time': time.time()
                       },
                       {
                           'id': 3,
                           'name': 'Virtual Visitas Test 2',
                           'displayName': 'Bill, Samantha, Paula',
                           'time': time.time()
                       },
                       {
                           'id': 2,
                           'name': 'Virtual Visitas Test 1',
                           'displayName': 'Paula, Bill, Samantha',
                           'time': time.time()
                       },
                       {
                           'id': 3,
                           'name': 'Virtual Visitas Test 2',
                           'displayName': 'Bill, Samantha, Paula',
                           'time': time.time()
                       }, {
                           'id': 2,
                           'name': 'Virtual Visitas Test 1',
                           'displayName': 'Paula, Bill, Samantha',
                           'time': time.time()
                       },
                       {
                           'id': 3,
                           'name': 'Virtual Visitas Test 2',
                           'displayName': 'Bill, Samantha, Paula',
                           'time': time.time()
                       },
                       {
                           'id': 2,
                           'name': 'Virtual Visitas Test 1',
                           'displayName': 'Paula, Bill, Samantha',
                           'time': time.time()
                       },
                       {
                           'id': 3,
                           'name': 'Virtual Visitas Test 2',
                           'displayName': 'Bill, Samantha, Paula',
                           'time': time.time()
                       }, {
                           'id': 2,
                           'name': 'Virtual Visitas Test 1',
                           'displayName': 'Paula, Bill, Samantha',
                           'time': time.time()
                       },
                       {
                           'id': 3,
                           'name': 'Virtual Visitas Test 2',
                           'displayName': 'Bill, Samantha, Paula',
                           'time': time.time()
                       }
                   ])

@app.route('/avail-convos', methods=['GET'])
def avail_convos():
    return jsonify(message=
                   [
                       {
                           'id': 4,
                           'name': 'Tennis Social #1',
                           'displayName': 'Tennis Social #1',
                           'time': time.time()
                       },
                       {
                           'id': 5,
                           'name': 'Tennis Social #2',
                           'displayName': 'Tennis Social #2',
                           'time': time.time()
                       }
                   ]), 200

@app.route('/organizations-old', methods=['GET'])
def organizations_old():
    return jsonify(message=
                   [
                       {
                           'id': 0,
                           'name': 'Harvard Class of 2024',
                           'displayName': 'Harvard Class of 2024'
                       }
                   ])

@app.route('/profile-old', methods=['GET', 'POST'])
def profile_old():
    return jsonify(message=
                   {
                       'email': 'albertzhang9000@gmail.com',
                       'displayName': 'Albert Zhang',
                       'state': 'Georgia',
                       'country': 'USA',
                       'participating': True,
                       'avatar': ''
                   }
    ), 200


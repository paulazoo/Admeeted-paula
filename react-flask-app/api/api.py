import time, json
from flask import Flask, jsonify, render_template, request, g
from flask_wtf import Form
from werkzeug import exceptions as wex
import db_for_flask

#%%
app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return jsonify({'time': time.time()})

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
@app.route('/login', methods=['POST'])
def login():
    '''
    Inputs will be a username (String) and password (String)
    Outputs will be whether user successfully logs in (Boolean)
    '''
    # Placeholder code
    loggedIn = True
    return jsonify(isLoggedIn=loggedIn), 200

# Bill's placeholder
@app.route('/logout', methods=['GET'])
def logout():
    loggedIn = False
    return jsonify(isLoggedIn=loggedIn), 200

'endpoint or route??'
@app.route('/profile', methods=['GET','POST'])
def profile():
    #user_uid = ...?
    user_uid=g.user_uid
    #if the profile form is edited and submitted
    if request.method == 'POST':
        profile_data = request.get_json()
        db_for_flask.profile_db(profile_data)
    
    profile_data=db_for_flask.db_profile(user_uid)
    
    return jsonify(message=profile_data), 200
  
    
@app.route('/profile/<int:other_user_uid>', methods=['GET'])
def other_profile(other_user_uid):
    
    profile_data=db_for_flask.db_profile(other_user_uid)
    
    return jsonify(message=profile_data), 200


@app.route('/upcoming-events', methods=['GET'])
def upcoming_events():
    user_uid=g.user_uid
    upcoming_events_data = db_for_flask.db_upcoming_events(user_uid)
    return jsonify(message=upcoming_events_data), 200

@app.route('/avail-events/<org_uid>', methods=['GET'])
def avail_events(org_uid):
    user_uid=g.user_uid
    avail_events_data = db_for_flask.db_avail_events(user_uid, org_uid)
    return jsonify(message=avail_events_data), 200
 
@app.route('/events/<event_uid>', methods=['GET', 'POST'])
def events(event_uid):
    user_uid=g.user_uid
    
    if request.method == 'POST':
        signup_cancel = request.get_json() #...sign up vs cancel?
        db_for_flask.events_db(user_uid, event_uid, signup_cancel)
    
    events_data = db_for_flask.db_events(event_uid)
    return jsonify(message=events_data), 200

@app.route('/conversations', methods=['GET'])
def convos():
    user_uid=g.user_uid
    convos_data = db_for_flask.db_convos(user_uid)
    return jsonify(message=convos_data), 200

@app.route('/conversations/<convo_uid>', methods=['GET'])
def other_convos(convo_uid):
    #...bc user can't change convos?
    user_uid=g.user_uid
    other_convos_data = db_for_flask.db_other_convos(user_uid, convo_uid)
    return jsonify(message=other_convos_data), 200

@app.route('/organizations', methods=['GET', 'POST'])
def orgs():
    user_uid=g.user_uid
    
    if request.method == 'POST':
        signup_cancel, org_uid = request.get_json() #...sign up vs cancel?
        db_for_flask.org_db(user_uid, org_uid, signup_cancel)
        

    orgs_data = db_for_flask.db_orgs(user_uid)
    return jsonify(message=orgs_data), 200

@app.route('/organizations/<org_uid>', methods=['GET', 'POST'])
def other_orgs(org_uid):
    user_uid=g.user_uid
    other_orgs_data = db_for_flask.db_other_orgs(user_uid, org_uid)
    return jsonify(message=other_orgs_data), 200

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
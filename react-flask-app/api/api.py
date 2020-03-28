import time, json
from flask import Flask, jsonify, request, g
# from flask_wtf import Form
from werkzeug import exceptions as wex
# import db_for_flask
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
#
# 'endpoint or route??'
# @app.route('/profile', methods=['GET','POST'])
# def profile():
#     #user_uid = ...?
#     user_uid=g.user_uid
#     #if the profile form is edited and submitted
#     if request.method == 'POST':
#         profile_data = request.get_json()
#         db_for_flask.profile_db(profile_data)
#
#     profile_data=db_for_flask.db_profile(user_uid)
#
#     return jsonify(message=profile_data), 200
#
#
# @app.route('/profile/<int:other_user_uid>', methods=['GET'])
# def other_profile(other_user_uid):
#
#     profile_data=db_for_flask.db_profile(other_user_uid)
#
#     return jsonify(message=profile_data), 200
#
#
# @app.route('/upcoming-events', methods=['GET'])
# def upcoming_events():
#     user_uid=g.user_uid
#     upcoming_events_data = db_for_flask.db_upcoming_events(user_uid)
#     return jsonify(message=upcoming_events_data), 200
#
# @app.route('/avail-events/<org_uid>', methods=['GET'])
# def avail_events(org_uid):
#     user_uid=g.user_uid
#     avail_events_data = db_for_flask.db_avail_events(user_uid, org_uid)
#     return jsonify(message=avail_events_data), 200
#
# @app.route('/events/<event_uid>', methods=['GET', 'POST'])
# def events(event_uid):
#     user_uid=g.user_uid
#
#     if request.method == 'POST':
#         signup_cancel = request.get_json() #...sign up vs cancel?
#         db_for_flask.events_db(user_uid, event_uid, signup_cancel)
#
#     events_data = db_for_flask.db_events(event_uid)
#     return jsonify(message=events_data), 200
#
# @app.route('/conversations', methods=['GET'])
# def convos():
#     user_uid=g.user_uid
#     convos_data = db_for_flask.db_convos(user_uid)
#     return jsonify(message=convos_data), 200
#
# @app.route('/conversations/<convo_uid>', methods=['GET'])
# def other_convos(convo_uid):
#     #...bc user can't change convos?
#     user_uid=g.user_uid
#     other_convos_data = db_for_flask.db_other_convos(user_uid, convo_uid)
#     return jsonify(message=other_convos_data), 200
#
# @app.route('/organizations', methods=['GET', 'POST'])
# def orgs():
#     user_uid=g.user_uid
#
#     if request.method == 'POST':
#         signup_cancel, org_uid = request.get_json() #...sign up vs cancel?
#         db_for_flask.org_db(user_uid, org_uid, signup_cancel)
#
#
#     orgs_data = db_for_flask.db_orgs(user_uid)
#     return jsonify(message=orgs_data), 200
#
# @app.route('/organizations/<org_uid>', methods=['GET', 'POST'])
# def other_orgs(org_uid):
#     user_uid=g.user_uid
#     other_orgs_data = db_for_flask.db_other_orgs(user_uid, org_uid)
#     return jsonify(message=other_orgs_data), 200

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
       'eventName': 'Virtual Visitas Test 1',
       'displayName': 'Paula, Bill, Samantha',
       'org': 0,
       'timeStart': time.time(),
       'timeEnd': time.time(),
       'link': 'https://hangouts.google.com/group/u5Dg6H94cGFjg9JaA'
   },
   {
       'id': 3,
       'eventName': 'Virtual Visitas Test 2',
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
def past_convos_org(org_uid):
    return jsonify(message=past_convos_old_data[org_uid]), 200

@app.route('/past-convos', methods=['GET'])
def past_convos():
    return jsonify(message=
                   [
                       {
                           'id': 2,
                           'eventName': 'Virtual Visitas Test 1',
                           'displayName': 'Paula, Bill, Samantha',
                           'org': 0,
                           'timeStart': time.time(),
                           'timeEnd': time.time(),
                           'link': 'https://hangouts.google.com/group/u5Dg6H94cGFjg9JaA'
                       },
                       {
                           'id': 3,
                           'eventName': 'Virtual Visitas Test 2',
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
    global profile_old_data
    if request.method == 'POST':
        print(request.get_json(force=True))
        profile_old_data['displayName'] = request.get_json(force=True)['new_data']['displayName']
        profile_old_data['state'] = request.get_json(force=True)['new_data']['state']
        profile_old_data['country'] = request.get_json(force=True)['new_data']['country']
        profile_old_data['interests'] = request.get_json(force=True)['new_data']['interests']
        return jsonify(message=True), 200
    return jsonify(message=profile_old_data), 200
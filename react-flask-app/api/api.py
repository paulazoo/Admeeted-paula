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


@app.route('/me', methods=['GET'])
def me():
    return jsonify(isLoggedIn=True), 200

#login

#logout

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
    
    return render_template('profile.html',profile_data=jsonify(profile_data))
  
    
@app.route('/profile/<int:other_user_uid>', methods=['GET'])
def other_profile(other_user_uid):
    
    profile_data=db_for_flask.db_profile(other_user_uid)
    
    return render_template('profile/<int:other_user_uid>.html',profile_data=jsonify(profile_data))


@app.route('/upcoming-events', methods=['GET'])
def upcoming_events():
    user_uid=g.user_uid
    upcoming_events_data = db_for_flask.db_upcoming_events(user_uid)
    return render_template('upcoming-events.html',upcoming_events_data=jsonify(upcoming_events_data))

@app.route('/avail-events/<org_uid>', methods=['GET'])
def avail_events(org_uid):
    user_uid=g.user_uid
    avail_events_data = db_for_flask.db_avail_events(user_uid, org_uid)
    return render_template('avail-events/<org_uid>.html',avail_events_data=jsonify(avail_events_data))
 
@app.route('/events/<event_uid>', methods=['GET', 'POST'])
def events(event_uid):
    user_uid=g.user_uid
    
    if request.method == 'POST':
        signup_cancel = request.get_json() #...sign up vs cancel?
        db_for_flask.events_db(user_uid, event_uid, signup_cancel)
    
    events_data = db_for_flask.db_events(event_uid)
    return render_template('upcoming-events.html',events_data=jsonify(events_data))

@app.route('/conversations', methods=['GET'])
def convos():
    user_uid=g.user_uid
    convos_data = db_for_flask.db_convos(user_uid)
    return render_template('conversations.html',convos_data=jsonify(convos_data))

@app.route('/conversations/<convo_uid>', methods=['GET'])
def other_convos(convo_uid):
    #...bc user can't change convos?
    user_uid=g.user_uid
    other_convos_data = db_for_flask.db_other_convos(user_uid, convo_uid)
    return render_template('conversations/<convo_uid>.html',other_convos_data=jsonify(other_convos_data))

@app.route('/organizations', methods=['GET', 'POST'])
def orgs():
    user_uid=g.user_uid
    
    if request.method == 'POST':
        signup_cancel, org_uid = request.get_json() #...sign up vs cancel?
        db_for_flask.org_db(user_uid, org_uid, signup_cancel)
        

    orgs_data = db_for_flask.db_orgs(user_uid)
    return render_template('organizations.html',orgs_data=jsonify(orgs_data))

@app.route('/organizations/<org_uid>', methods=['GET', 'POST'])
def other_orgs(org_uid):
    user_uid=g.user_uid
    other_orgs_data = db_for_flask.db_other_orgs(user_uid, org_uid)
    return render_template('organizations/<org_uid>.html',other_orgs_data=jsonify(other_orgs_data))

    
@app.route('/upcoming-convos')
def upcoming_convos():
    return jsonify(message=
        [
            {
                'id': 0,
                'name': 'Coca-Cola Scholars 2020',
                'time': time.time()
            },
            {
                'id': 1,
                'name': 'Virtual Visitas',
                'time': time.time()
            }
        ]
    ), 200


@app.route('/login', methods=['POST'])
def login():
    # Placeholder code
    return jsonify(isLoggedIn=True), 200

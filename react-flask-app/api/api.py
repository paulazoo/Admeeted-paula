import time, json
from flask import Flask, jsonify, render_template, request
from werkzeug import exceptions as wex

# from flask_login import (
#     LoginManager,
#     current_user,
#     login_required,
#     login_user,
#     logout_user,
# )
#
# from oauthlib.oauth2 import WebApplicationClient
# import requests


# # Configuration
# GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
# GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
# GOOGLE_DISCOVERY_URL = (
#     "https://accounts.google.com/.well-known/openid-configuration"
# )
#
# # User session management setup
# # https://flask-login.readthedocs.io/en/latest
# login_manager = LoginManager()
# login_manager.init_app(app)
#
# # Naive database setup
# try:
#     init_db_command()
# except sqlite3.OperationalError:
#     # Assume it's already been created
#     pass
#
# # OAuth 2 client setup
# client = WebApplicationClient(os.environ.get("GOOGLE_CLIENT_ID", None))
#
# # Flask-Login helper to retrieve a user from our db
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return jsonify({'time': time.time()})

@app.route('/register', methods=['POST'])
def register():
    #Under construction...
    try:
        data = request.get_json()
    except wex.BadRequest:
        return f.error(1313, "Bad request. Make sure your request conforms to the api."), 400
    return 'work in progresss'

@app.route('/hitest')
def hi():
    return "<h1>Hiiiii!!!</h1>"

@app.route('/profile', methods=['GET', 'POST'])
def profile():
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

@app.route('/upcoming-convos', methods=['GET'])
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

@app.route('/organizations', methods=['GET'])
def organizations():
    return jsonify(message=
                   [
                       {
                           'id': 0,
                           'name': 'Harvard Class of 2024',
                           'displayName': 'Harvard Class of 2024'
                       }
                   ])

loggedIn = False

@app.route('/me', methods=['GET'])
def me():
    '''
    Inputs: None
    Outputs: Whether user is currently logged in (Boolean)
    '''
    # placeholder code
    return jsonify(isLoggedIn=loggedIn), 200

@app.route('/login', methods=['POST'])
def login():
    '''
    Inputs will be a username (String) and password (String)
    Outputs will be whether user successfully logs in (Boolean)
    '''
    # Placeholder code
    loggedIn = True
    return jsonify(isLoggedIn=loggedIn), 200

@app.route('/logout', methods=['GET'])
def logout():
    loggedIn = False
    return jsonify(isLoggedIn=loggedIn), 200
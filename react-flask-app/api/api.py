import time, json
from flask import Flask, jsonify, render_template, request
from werkzeug import exceptions as wex

import firebase_admin
from firebase_admin import credentials

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

cred = credentials.Certificate("admeet2024-firebase-adminsdk-oa4v1-1a11cd5d5a.json")
firebase_admin.initialize_app(cred)


app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return jsonify({'time': time.time()})

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
    except wex.BadRequest:
        return f.error(1313, "Bad request. Make sure your request conforms to the api."), 400


    return 'work in progresss'

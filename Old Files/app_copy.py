# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:19:59 2020

@author: Samantha
"""
#For Google authentication

# Python standard libraries
import json
import os

# Third-party libraries
from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

# Internal imports
from db import init_db_command
from user import User

#%%
# Configuration
"""
Storing the Google Client ID and Client Secret 
(from https://console.developers.google.com/  Credentials for this project)
App gets client credentials by reading environmental variables

Windows users: set GOOGLE_CLIENT_ID=your_client_id in Command Prompt
"""
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)



"""
Below: Global variables and some naive database initialization logic. 
Other than the db initialization, this is the standard way 
to set up Flask, Flask-Login, and OAuthLib,

"""

# Flask app setup
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

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
                current_user.name, current_user.email, current_user.profile_pic
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
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
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


#To run your Flask application on your local computer to test the login flow
if __name__ == "__main__":
    app.run(ssl_context="adhoc")
    print("running")
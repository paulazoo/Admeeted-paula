# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:14:59 2020

@author: Samantha
"""

"""
User class will store and retrieve information from the SQL database. 
The name, email, and profile picture will all be retrieved from Google.

 User class has methods to get an existing user from the 
 database and create a new user.
"""
#For Google authentication

from flask_login import UserMixin
#import sqlite3
from db import get_db
#from db import init_db

class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):
        print("Get User Id")
        db = get_db()
        print("get user_id db gotten")

        a_user = db.child("users").child(user_id).get().val()
        print("User gotten from db from user_id: {} is: {}".format(user_id, a_user))

        print("Get User ID gotten from firebase")

        if not a_user:
            print("Get User ID no user")
            return None

        a_user = User(
            id_ = user_id, email = a_user['email'], name = a_user['name'], profile_pic = a_user['profile_pic']
        )
        print("Get User ID User: {}".format(a_user))
        return a_user

    @staticmethod
    def create(id_, name, email, profile_pic):
        print("Creating user")
        id_ = str(id_) #actually an integer (always 21 digits?)
        name = str(name) #already a string?
        email = str(email) #aleady a string?
        profile_pic = str(profile_pic) #already a string?
        db=get_db()
        user_dict = {'id_': id_, 'name': name, 'email': email, 'profile_pic':profile_pic}
        print("In create_user made this user_dict: {}".format(user_dict))
        db.child("users").child(id_).set(user_dict)
        
        
"""
Executes SQL statements against the database, 
which is retrieved from the get_db() function from db.py.
Each new user results in the insertion of an additional row in the database.
"""
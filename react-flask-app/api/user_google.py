# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:14:59 2020

@author: Samantha
"""
from db import get_db

"""
User class will store and retrieve information from the SQL database. 
The name, email, and profile picture will all be retrieved from Google.

 User class has methods to get an existing user from the 
 database and create a new user.
"""
#For Google authentication

from flask_login import UserMixin
import sqlite3
#import schema

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
        print("Get User ID database gotten")
        #init_db()
        a_user = db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()
        print("Get User ID user fetched")
        if not a_user:
            print("Get User ID no user")
            return None

        a_user = User(
            id_=a_user[0], name=a_user[1], email=a_user[2], profile_pic=a_user[3]
        )
        print("Get User ID User:")
        print(a_user)
        return a_user

    @staticmethod
    def create(id_, name, email, profile_pic):
        print("Create User staticmethod called")
        db = get_db()
        db.execute(
            "INSERT INTO user (id, name, email, profile_pic) "
            "VALUES (?, ?, ?, ?)",
            (id_, name, email, profile_pic),
        )
        db.commit()
        
"""
Executes SQL statements against the database, 
which is retrieved from the get_db() function from db.py.
Each new user results in the insertion of an additional row in the database.
"""
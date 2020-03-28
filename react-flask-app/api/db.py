# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:06:49 2020

@author: Samantha
"""
#Database for Google Authentication
# http://flask.pocoo.org/docs/1.0/tutorial/database/

#import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
import os 
import pyrebase

#def close_db(e=None):
    #TODO need a close_db?
    #db = g.pop("db", None)

    #if db is not None:
        #db.close()
def get_db():
    if "db" not in g:
        g.db=init_db()
    return g.db

def init_db():
    print("init db called")
    if "db" not in g:
        print("db not in g")
        project_id='admeeted-18732'
        config = {
           "apiKey": 'AIzaSyDyR1tbXRFE2fgENNTeepPyrCBExQ06rsk',
           "authDomain": project_id+".firebaseapp.com",
           "databaseURL": "https://"+project_id+".firebaseio.com",
           "projectId": project_id,
           "storageBucket": project_id+".appspot.com",
           "serviceAccount": r"", #Fill this in
           "messagingSenderId": "667088492207"
        }   

        firebase = pyrebase.initialize_app(config)
        g.db = firebase.database()
    return g.db
    #db = get_db()

    #with current_app.open_resource("schema.sql") as f:
        #db.executescript(f.read().decode("utf8"))

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    print("init db command")
    init_db()
    click.echo("Initialized the database.")

def init_app(app):
    #app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    
#schema.sql will execute this SQL to to create table in database
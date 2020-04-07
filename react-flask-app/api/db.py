#%%
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:06:49 2020

@author: Samantha
"""
#Database for Google Authentication
# http://flask.pocoo.org/docs/1.0/tutorial/database/

#import sqlite3
import time
import click
from flask import current_app, g
from flask.cli import with_appcontext
import pyrebase
import os

#def close_db(e=None):
    #TODO need a close_db?
    #db = g.pop("db", None)

    #if db is not None:
        #db.close()

def get_db():
    db=init_db()
    return db

def init_db():

    project_id='admeeted-paula'
    config = {
        "apiKey": 'AIzaSyDyuvwH7_J-8PMHK2g89IvePgWfpPsrY1A',
        "authDomain": project_id+".firebaseapp.com",
        "databaseURL": "https://"+project_id+".firebaseio.com",
        "projectId": project_id,
        "storageBucket": project_id+".appspot.com",
        # "serviceAccount": r"C:\Users\Samantha\Admeeted\Admeeted2.0\Admeeted\react-flask-app\api\admeeted-private-key.json", #Fill this in
        # "serviceAccount": r"C:\Users\billz\PycharmProjects\VirtualVisitas\Admeeted\react-flask-app\api\admeeted-private-key.json",
        #"serviceAccount": str(os.getcwd()) + r"/admeeted-private-key.json",
            "serviceAccount": r'C:\Users\pkzr3\Admeeted-paula\react-flask-app\api\admeeted-paula-private-key.json',
        "messagingSenderId": "785353783740"
    }
    print(config['serviceAccount'])

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    return db
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
    
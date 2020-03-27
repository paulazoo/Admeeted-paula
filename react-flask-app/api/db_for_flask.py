#%%
import os
import pyrebase

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
db = firebase.database()
#%%

def profile_db(data):
    
    return data

def db_profile(user_uid):
    data = db.child('users').child(user_uid).get().val()

    return data

def db_upcoming_events(user_uid):
    #possibly by time upcoming?
    data=db.child('events_users').child(user_uid).get().val()
    return data

def db_avail_events(user_uid, org_uid):
    #possibly by time upcoming?
    signed_up=dict(db.child('events_users').child(user_uid).get().val())
    org_events=dict(db.child('events_orgs').child(org_uid).get().val())
    data_set = set(org_events)-set(signed_up)
    data=dict.fromkeys(data_set, True)
    return data

def events_db(user_uid,event_uid,signup_cancel):
    if signup_cancel == 'signup':
        db.child("events_users").child(user_uid).set({event_uid:True})
        db.child("users_events").child(event_uid).set({user_uid:True})
    elif signup_cancel == 'cancel':
        db.child("events_users").child(user_uid).remove({event_uid:True})
        db.child("users_events").child(event_uid).remove({user_uid:True})
    
    
def db_events(event_uid):
    data = db.child('events').child(event_uid).get().val()
    return data

def db_convos(user_uid):
    data = db.child('convos_users').child(user_uid).get().val()
    return data

def db_other_convos(user_uid, convo_uid):
    data = db.child('convos').child(convo_uid).get().val()
    return data

def orgs_db(user_uid,org_uid,signup_cancel):
    if signup_cancel == 'signup':
        db.child("orgs_users").child(user_uid).set({org_uid:True})
        db.child("users_orgs").child(org_uid).set({user_uid:True})
    elif signup_cancel == 'cancel':
        db.child("orgs_users").child(user_uid).remove({org_uid:True})
        db.child("users_orgs").child(org_uid).remove({user_uid:True})
    
def db_orgs(user_uid):
    data = db.child('orgs_users').child(user_uid).get().val()
    return data

def db_other_orgs(user_uid, org_uid):
    data = db.child('orgs').child(org_uid).get().val()
    return data
#%%

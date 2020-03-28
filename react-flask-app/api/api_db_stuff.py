# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:43:31 2020

@author: pkzr3
"""

from datetime import datetime
#%%
user=db.child('users').child(user_uid).get().val()

majors=list(db.child('major_user').child(user_uid).get().val().keys())

data={'name':user['name'], 
 'displayName':user['displayName'],
 'state':user['state'],
 'country':user['country'],
 'avatar':user['avatar'],
 'major':majors
 }
#%%
db.child('users').child(user_uid).set({
        'displayName':pdata['displayName'],
        'state':pdata['state'],
        'country':pdata['country'],
        })

majors=pdata['major']
majors_dict=dict.fromkeys(majors, True)

db.child('major_user').child(user_uid).set(majors_dict)
for major in majors:
    db.child('user_major').child(major).set({user_uid: True})

#%%
events=db.child('events_users').child(user_uid).get().val()
events_info=[]
for event in events:
    event_info_ord=db.child('events').child(event).get().val()
    event_timeStart=datetime.strptime(event_info_ord['timeStart'], '%H:%M %d %B %Y')

    if event_timeStart<=datetime.now():
        event_info=dict(event_info_ord)
        event_info.update({'event_uid':event})
        events_info.append(event_info)
    
    #%%
db.child("events").remove()
#%%
events_users=db.child('events_users').child(user_uid).get().val()
events_orgs=db.child('events_orgs').child(org_uid).get().val()
events=set(events_users) & set(events_orgs)
events_info=[]
for event in events:
    event_info_ord=db.child('events').child(event).get().val()
    event_timeStart=datetime.strptime(event_info_ord['timeStart'], '%H:%M %d %B %Y')

    if event_timeStart<=datetime.now():
        event_info=dict(event_info_ord)
        event_info.update({'event_uid':event})
        events_info.append(event_info)
#%%
events_users=db.child('events_users').child(user_uid).get().val()
events_orgs=db.child('events_orgs').child(org_uid).get().val()
events=set(events_orgs) - set(events_users)
data=[]
for event in events:
    event_info_ord=db.child('events').child(event).get().val()
    event_timeStart=datetime.strptime(event_info_ord['timeStart'], '%H:%M %d %B %Y')

    if event_timeStart<=datetime.now():
        event_info=dict(event_info_ord)
        event_info.update({'event_uid':event})
        data.append(event_info)

#%%
orgs=db.child('org_user').child(user_uid).get().val()
all_events={}
for org in orgs:
    org_events=db.child('events_orgs').child(org).get().val()
    all_events.update(dict(org_events))
events=set(all_events) - set(events_users)
data=[]
for event in events:
    event_info_ord=db.child('events').child(event).get().val()
    event_timeStart=datetime.strptime(event_info_ord['timeStart'], '%H:%M %d %B %Y')

    if event_timeStart<=datetime.now():
        event_info=dict(event_info_ord)
        event_info.update({'event_uid':event})
        data.append(event_info)

#%%
event_info=dict(db.child('events').child(event_uid).get().val())
event_info.update({'event_uid':event_uid})

#%%
if signup_cancel==True:
    db.child('event_user').child(user_uid).update({event_uid:True})
    db.child('user_event').child(event_uid).update({user_uid:True})
elif signup_cancel==False:
    db.child('event_user').child(user_uid).update({event_uid: None})
    db.child('user_event').child(event_uid).update({user_uid: None})
#%%
convos=db.child('convo_user').child(user_uid).get().val()
data={}
for convo in convos:
    convo_info=db.child('convos').child(convo).get().val()
    convo_info.update({'convo_uid': convo})
    data.update(convo_info)
#%%
org_uid='Harvard'
org_info=dict(db.child('orgs').child(org_uid).get().val())
org_info.update({'org_uid':org_uid, 'admin':True})
org_users=db.child('user_org').child(org_uid).shallow().get().val()
if str(user_uid) in org_users:
    org_info.update({'joined':True})
    
#%%
if signup_cancel==True:
    db.child('org_user').child(user_uid).update({org_uid:True})
    db.child('user_org').child(org_uid).update({user_uid:True})
elif signup_cancel==False:
    db.child('org_user').child(user_uid).update({org_uid: None})
    db.child('user_org').child(org_uid).update({user_uid: None})
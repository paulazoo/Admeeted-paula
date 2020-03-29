#%%
#password = "DONT_YOU_DARE_STEAL_MY_PW!"
#I'm creating a new email and GroupMe account for this lol
#I'm thinking of naming it sambot but lmk if you want it to be
#something more official haha


'''
import pandas as pd 
import numpy as np
import time
import webbot
from webbot import Browser
from selenium.webdriver.common.keys import Keys
#print("hello world")
samantha_array = pd.Series(["hi", "thank", "you", "so", "much"])
print(type(samantha_array))
print(samantha_array)
web = Browser()
#web.driver.get("https://www.google.com")
web.driver.get("https://web.groupme.com/signin")
time.sleep(1)
web.driver.find_element_by_id("signinUserNameInput").send_keys("sammie7242@gmail.com")
web.driver.find_element_by_id("signinPasswordInput").send_keys(password)
web.driver.find_element_by_id("signinPassWordInput").send_keys(Keys.RETURN)
'''
#%%
"""
#Testing def organizations(): from api.py
import click
from flask import current_app, g
from flask.cli import with_appcontext
import os 
import pyrebase



print("init db called")
project_id='admeeted-18732'
config = {
           "apiKey": 'AIzaSyDyR1tbXRFE2fgENNTeepPyrCBExQ06rsk',
           "authDomain": project_id+".firebaseapp.com",
           "databaseURL": "https://"+project_id+".firebaseio.com",
           "projectId": project_id,
           "storageBucket": project_id+".appspot.com",
           "serviceAccount": r"",
           "messagingSenderId": "667088492207"
}   

firebase = pyrebase.initialize_app(config)
db = firebase.database()


org_info_list = [] #list of dictionaries containg info for each of a user's orgs
user_uid= 10
#db=get_db()
'''
Inputs: user_uid
Outputs: a list containing the info (in dicts) for all of a user's organizations
'''
org_info_list = [] #list of dictionaries containg info for each of a user's orgs
#user_uid=session.get('user_uid')
user_orgs = dict(db.child('org_user').child(user_uid).get().val())
if user_orgs:
    for key in user_orgs:
        #where key is an org
        dictionary = dict(db.child('orgs').child(key).get().val())
        dictionary['id'] = key
        org_info_list.append(dictionary)
elif not user_orgs:
    org_info_list=[]

#return jsonify(message=org_info_list), 200

    
print("Final list: {}".format(org_info_list))
"""
#%%
#Starting with organization uid, outputting emails grouped by major
import click
from flask import current_app, g
from flask.cli import with_appcontext
import os 
import pyrebase
import random

print("init db called")
project_id='admeeted-18732'
config = {
           "apiKey": 'AIzaSyDyR1tbXRFE2fgENNTeepPyrCBExQ06rsk',
           "authDomain": project_id+".firebaseapp.com",
           "databaseURL": "https://"+project_id+".firebaseio.com",
           "projectId": project_id,
           "storageBucket": project_id+".appspot.com",
           "serviceAccount": r"",
           "messagingSenderId": "667088492207"
}   

firebase = pyrebase.initialize_app(config)
db = firebase.database()

org_uid = "Harvard"
event_uid='Harvard Admeeted 2024 3-30'
print("Org Uid: %s Event Uid: %s" % (org_uid, event_uid))
users_list = list(db.child('user_event').child(event_uid).shallow().get().val())
#print("Users List: {}".format(users_list))
majors_list = list(db.child('major_org').child(org_uid).shallow().get().val())
#print("Majors List: {}".format(majors_list))

users_majors_list = []
users_majors_dict = {} #dict where key is user uid and value is their list of majors
update_users_majors_dict = {} #final dict with key: user and value: one random major in org

for user in users_list:
    #This is a list of all the majors one user has (not specific to org)
    all_majors = db.child('major_user').child(user).shallow().get().val()
    if all_majors:
        all_majors_list=list(all_majors)
        #Remove majors not in org then incorporate
        all_majors_org = [x for x in all_majors if x in majors_list]
        #Currently getting a dictionary with each key as user id and each value as their majors
        rand_major = random.choice(all_majors_org)
        #print(rand_major)
        #print("All Majors after random_major function is: {}".format(all_majors))
        update_users_majors_dict[user] = rand_major
        #print("Update Users Majors Dict is: {}".format(update_users_majors_dict))
    elif not all_majors:
        update_users_majors_dict[user]='No major'

#Now taking completed update_users_majors_dict and resorting to
    #key: major in that dict, value: all names with that major
    #Make this one into a list of one-key dicts? (Other one not import I'm gonna erase previous options)
resorted_dict = {}
for user in update_users_majors_dict:
    major = update_users_majors_dict[user]
    if major not in resorted_dict:
        #print("Major not in resorted_dict, adding key")
        resorted_dict[major] = []
    resorted_dict[major].append(user)
    #print("Resorted dict is: {}, at user: {}, with major: {}".format(resorted_dict, user, major))

    

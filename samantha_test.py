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
from random import randint

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

    #Pick a random major
def random_major(list_majors):
    rand_int = randint(0, (len(list_majors)-1))
    selected = list_majors[rand_int]
    print("Random_major function result is: {}".format(selected))
    return selected

org_uid = "Harvard"
print("Org Uid: {}".format(org_uid))
users_list = list(db.child('user_org').child(org_uid).get().val().keys())
print("Users List: {}".format(users_list))
majors_list = ["Biology", "Computer Science", "English", "History", "Music", "Neuroscience", "Psychology"]
print("Majors List: {}".format(majors_list))

users_majors_list = []
users_majors_dict = {} #dict where key is user uid and value is their list of majors
update_users_majors_dict = {} #final dict with key: user and value: one random major in org

for user in users_list:
    all_majors = [] #This is a list of all the majors one user has (not specific to org)
    all_majors = list(db.child('major_user').child(user).get().val().keys())
    print("At user: {}, List of all majors is: {}".format(user, all_majors))

    #Remove majors not in org then incorporate
    for major in all_majors:
        if major not in majors_list:
            print("Major {} not in org's majors".format(major))
            all_majors.remove(major)
            print("All majors list is: {} with major {} removed".format(all_majors, major))

    users_majors_dict[user] = all_majors
    print("Users Majors Dict is: {}".format(users_majors_dict))
    
    #Currently getting a dictionary with each key as user id and each value as their majors
    all_majors = random_major(all_majors)
    print("All Majors after random_major function is: {}".format(all_majors))
    update_users_majors_dict[user] = all_majors
    print("Update Users Majors Dict is: {}".format(update_users_majors_dict))
    

#Now taking completed update_users_majors_dict and resorting to
    #key: major in that dict, value: all names with that major
    #Make this one into a list of one-key dicts? (Other one not import I'm gonna erase previous options)
resorted_dict = {}
for user in update_users_majors_dict:
    major = update_users_majors_dict[user]

    if major not in resorted_dict:
        print("Major not in resorted_dict, adding key")
        add_list = [user]
        resorted_dict[major] = add_list
        
    else:
        print("Major key in resorted_dict, appending user to value list")
        resorted_dict[major] = list(resorted_dict[major]).append(user)
    print("Resorted dict is: {}, at user: {}, with major: {}".format(resorted_dict, user, major))

    

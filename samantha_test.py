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
#%%
import os
import pyrebase
#fb_conn=fb.FirebaseApplication('https://admeet2024.firebaseio.com/organizations/yx4uGm90iuD1BOOpNwEw', None)
project_id='admeeted-18732'
config = {
  "apiKey": 'AIzaSyDyR1tbXRFE2fgENNTeepPyrCBExQ06rsk',
  "authDomain": project_id+".firebaseapp.com",
  "databaseURL": "https://"+project_id+".firebaseio.com",
  "projectId": project_id,
  "storageBucket": project_id+".appspot.com",
  "serviceAccount": r"C:\Users\pkzr3\Admeeted\react-flask-app\api\admeeted-private-key.json",
  "messagingSenderId": "667088492207"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#%%
from config_db import MyParser

#Iterates through the spreadsheet rows and creates a list of user objects for Harvard
myparser = MyParser("Harvard.xlsx")
df=myparser.all_summary
h_dict=df.to_dict(orient='records')

#%%
def all_childs(person):
    user_keys = ['user_uid','name', 'email', 'state', 'country', 'participating', 'grade']
    user_dict={ key : person[key]  for key in user_keys[1:6] }
    
    return user_dict    

#%%
#user_id cant have .
def add_user(peeps):
    for person in peeps:
        user_id=person['user_uid']
        print(user_id)
        user_child = all_childs(person)
        #print(user_child)
        db.child("users").child(user_id).set(user_child)

#%%
#no / in any answers
#careful ,
def add_multi_users(peeps, multi):
    for person in peeps:
        user_id=person['user_uid']
        #print(user_id)
        multi_users_child={}
        multi_list=person[multi].split(", ")
        for multi_val in multi_list:
            #print(multi_val)
            multi_users_child.update({multi_val : True})
            #print(multi_users_child)
        #print(multi_users_child)
        db.child(multi.lower()+"_user").child(user_id).set(multi_users_child)

#%%
import random
def add_users_multi(peeps, multi_strs, multi):
    
    for multi_uid in multi_strs:
        multi_users_child={}
        
        for person in peeps:
            if multi_uid in person[multi].split(","):
                multi_users_child.update({person['user_uid'] : True})
        
        db.child("user_"+multi.lower()).child(multi_uid).set(multi_users_child)

    
#%%       
db.child("Harvard").remove()

#%%
db.child("organizations").child("Harvard").set({'org_name':'Harvard 2024', 'date_founded':'24 March 2020'})
#%%
multi='org'
category_summary = df[multi]

#turn each multichoose answer into a list of chosen multichoose answers
category_list = [(category_summary[i].split(", ")) for i in range(0,len(category_summary))]

#get only the first ans for ans with multichoose...
category_firsts=[random.choice(ans) for ans in category_list]

#get all existing values in the category w no duplicates
multi_strs=list(set(category_firsts))

#%%
# if request.auth != null;
storage=firebase.storage()
storage.child("org_imgs/harvard_org_img.png").put('harvard_org_img.png')

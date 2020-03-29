#%%
import os
import random
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
#%%
firebase = pyrebase.initialize_app(config)
#%%
db = firebase.database()

#%%
from config_db import MyParser

#Iterates through the spreadsheet rows and creates a list of user objects for Harvard
myparser = MyParser("setting_majors.xlsx")
df=myparser.all_summary
major_dict=df.to_dict(orient='records')

#%%
def all_childs(person):
    #user_keys = ['user_uid','name', 'email', 'state', 'country', 'participating', 'grade']
    user_keys = ['major','displayName','description']
    
    user_dict={ key : person[key]  for key in user_keys[1:6] }
    
    return user_dict    

#%%
#user_id cant have .
def add_user(peeps):
    for person in peeps:
#        user_id=person['user_uid']
        user_id=person['major']
#        print(user_id)
        user_child = all_childs(person)
        #print(user_child)
        db.child("majors").child(user_id).update(user_child)

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
db.child("orgs").child("Harvard").update({'displayName':'Harvard 2024', 
        'dateFounded':'24 March 2020',
        'description': 'Group for connecting pre-first year students!'
        })
db.child("orgs").child("UVA").update({'displayName':'University of Virginia 2024', 
        'dateFounded':'28 March 2020', 
        'avatar':'<UVA_pic_link>',
        'description': 'Group for connecting pre-first year students!'
        })

#%%
multi='interest'
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
#%%
db.child('majors').child('Neuroscience').set({'displayName':'Neuroscience','description':'Best science in the world!'})
db.child('majors').child('Psychology').set({'displayName':'Psychology','description':'Study of the mind...'})

#%%
#%%
db.child("events").child("Harvard Admeeted 2024 3-25").set({
        'displayName': 'Virtual Visitas 25',
        'org': 'Harvard',
		'timeCreated': '11:00 23 March 2020' ,
		'timeStart': '16:00 27 March 2020' ,
		'timeEnd': '18:00 27 March 2020' ,
		'creator': 1,
		'desired_size': 3,
		'num_rounds': 4})

    #%%
db.child('user_event').child("Harvard Admeeted 2024 3-25").set({10:True})
#%%
db.child('event_user').child(10).set({"Harvard Admeeted 2024 3-25":True})

#%%
db.child('event_org').child('Harvard').set({"Harvard Admeeted 2024 3-25":True, "Harvard Admeeted 2024 3-26":True,"Harvard Admeeted 2024 3-27":True})

#%%
db.child('org_user').child(10).set({'Harvard':True})

#%%
db.child('user_org').child('Harvard').set({10:True})

#%%
data={
      'displayName': 'Albert, Samantha, Paula, Bill',
      'org': 'Harvard',
      'link': '<Hangouts Chat URL>',
      'timeStart': '16:00 27 March 2020',
      'timeEnd': '18:00 27 March 2020',
      'members': {
			1: True,
            10: True,
            }
      }
db.child('convos').child('our_convo').set(data)
#%%
db.child('user_convo').remove()
convo_uid='our_convo'
#%%
db.child('convo_user').child(1).set({convo_uid:True})
#%%
major_org_dict=dict.fromkeys(df['major'],True)
db.child('major_org').child('Harvard').update(major_org_dict)
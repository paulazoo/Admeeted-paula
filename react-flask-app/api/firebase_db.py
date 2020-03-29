#%%
import os
import pyrebase
import random
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
def get_emails(user_list):
    email_dict={}
    for user_uid in user_list:
        email_dict.update({user_uid:db.child('users').child(user_uid).child('email').get().val()})
    return email_dict

#%%
def get_all_users():
    #starting hey
    users = db.child("users").shallow().get().val()
    #print(org_users)
    if users:
        users=list(users)
    elif not users:
        users=[]
    return users    

#%%
def get_org_users(org_uid, event_uid): 
    #starting hey
    org_users = db.child("user_org").child(org_uid).shallow().get().val()
    #print(org_users)
    if org_users:
        org_users=list(org_users)
    elif not org_users:
        org_users=[]
    return org_users

#%%
def get_major_users(org_uid,event_uid):
    #org_uid = "Harvard"
    #event_uid='Harvard Admeeted 2024 3-30'
    print("Org Uid: %s Event Uid: %s" % (org_uid, event_uid))
    users_list = list(db.child('user_event').child(event_uid).shallow().get().val())
    #print("Users List: {}".format(users_list))
    majors_list = list(db.child('major_org').child(org_uid).shallow().get().val())
    #print("Majors List: {}".format(majors_list))

    update_users_majors_dict = {} #final dict with key: user and value: one random major in org
    
    for user in users_list:
        #This is a list of all the majors one user has (not specific to org)
        all_majors = db.child('major_user').child(user).shallow().get().val()
        if all_majors:
            #Remove majors not in org then incorporate
            all_majors_org = [major for major in all_majors if major in majors_list]
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
        
    return resorted_dict
        #print("Resorted dict is: {}, at user: {}, with major: {}".format(resorted_dict, user, major))

#%%
def get_event_info(event_uid):
    #event_uid='Harvard Admeeted 2024 3-30'
    event_info=db.child('events').child(event_uid).get().val()
    return event_info

#%%
link='<link>'

def post_convo(giant_dict, event_uid, event_info):
    for convo in giant_dict:
        #possibly change displayName
        db.child('convos').child(convo).update({'displayName':convo, 
                'event':event_uid,
                'link':link,
                'org':event_info['org'],
                'timeStart':event_info['timeStart'],
                'timeEnd':event_info['timeEnd'],
                'members':dict.fromkeys(giant_dict[convo].keys(), True)
                })
            
        db.child('convo_event').child(event_uid).update({convo:True})
        for user_uid in giant_dict[convo].keys():
            db.child('convo_user').child(user_uid).update({convo:True})   
    return True

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
org_users_ref=db.child("org_users").get()
print(org_users_ref.val())

#%%
def find_user_by(child, value):
    users_by_name = db.child("users").order_by_child(child).equal_to(value).get().val()
    return users_by_name
#%%
def get_college_emails(college_name): 
    #starting hey
    all_emails=[]
    college_users = db.child("organizations").child(college_name).shallow().get().val()
    for user_in_org in college_users:
        user_dict=find_user_by("fullname",user_in_org)
        all_emails.append(user_dict[user_in_org]['email_address'])
    return all_emails

#%%
    





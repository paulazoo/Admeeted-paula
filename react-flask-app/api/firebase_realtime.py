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
ab_dict={'a':'b'}
#%%
new_event = ab_dict
db.child("events").push(new_event)

#%%
data = {"name": "Mortimer 'Morty' Smith", 'blah':'hey'}
db.child("users").child("Morty").set(data)

#%%
etag = db.child("users").child("Morty").get_etag()
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").child("Morty").conditional_set(data, etag)

#%%
from config import ExcelParser

#Iterates through the spreadsheet rows and creates a list of user objects for Harvard
myparser = ExcelParser("Harvard.xlsx")
df=myparser.all_summary    
#users.append(User(user['fullname'], user['Email Address'], 'Harvard', user['Timestamp'], 2024, user['From'], strToTuple(user['Major']), (), strToTuple(user['What genres of music do you like?']), strToTuple(user['What sports are you interested in?']), strToTuple(user['What are some of your interests or hobbies?']), user['Feedback :)'] if user['Feedback :)']==user['Feedback :)'] else None))

for index, row in df.iterrows():
    print(row['fullname'])

h_dict=df.to_dict(orient='records')

#%%
def df_org(df, college):
    df_college=df[df['organization'].str.contains(college)]
    college_dict={}
    for fullname in df_college['fullname']:
        college_dict.update({ fullname : True})
        #print(college_dict)
    db.child("organizations").child(college).set(college_dict)
    return college_dict

#%%
def all_childs(person):
    user_keys = ['fullname', 'email_address', 'from', 'participating']
    user_dict={ key : person[key]  for key in user_keys }
    
    return user_dict    

#%%
#user_id cant have .
def add_user(peeps):
    for person in peeps:
        user_id=person['fullname']
        print(user_id)
        user_child = all_childs(person)
        print(user_child)
        db.child("users").child(user_id).set(user_child)

#%%
def add_org_users(peeps):
    for person in peeps:
        user_id=person['fullname']
        print(user_id)
        org_users_child={}
        for org in person['organization'].split(", "):
            org_users_child.update({org : True})
            print(org_users_child)
        print(org_users_child)
        db.child("org_users").child(user_id).set(org_users_child)
        
#%%
def add_org():
    for person in peeps:
        user_id=person['fullname']
        print(user_id)
        org_users_child={}
        for org in person['organization'].split(", "):
            org_users_child.update({org : True})
            print(org_users_child)
        print(org_users_child)
        db.child("org_users").child(user_id).set(org_users_child)
        
        #%%
#no / in any answers
#careful ,
def add_any(peeps, multi):
    for person in peeps:
        user_id=person['fullname']
        print(user_id)
        multi_users_child={}
        multi_list=person[multi].split(", ")
        for multi_val in multi_list:
            print(multi_val)
            multi_users_child.update({multi_val : True})
            print(multi_users_child)
        print(multi_users_child)
        db.child(multi.lower()).child(user_id).set(multi_users_child)
        
#%%
#lol restart
for person in h_dict:
    fullname=person['fullname']
    db.child("users").child(fullname).remove()

#%%
db.child("users").remove()
#%%
multi='Major'
for person in h_dict:
    multi_list=person[multi].split(", ")
    print(multi_list)
    
#%%
org_users_ref=db.child("org_users").get()
print(org_users_ref.val())

#%%
def find_user_by(child, value):
    users_by_name = db.child("users").order_by_child(child).equal_to(value).get()
    return users_by_name
#%%
#starting hey
all_emails[]
college_users = db.child("organizations").child("Harvard").shallow().get().val().tolist()
for user_in_org in college_users:
    user_dict=find_user_by("fullname",user_in_org)
    all_emails.append(user_dict[user_in_org]['email_address'])

    





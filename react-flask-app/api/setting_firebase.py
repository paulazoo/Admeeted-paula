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

#Iterates through the spreadsheet rows and creates a list of user objects
myparser = MyParser("setting_firebase_excel.xlsx")
df=myparser.all_summary    

for index, row in df.iterrows():
    print(row['fullname'])

h_dict=df.to_dict(orient='records')

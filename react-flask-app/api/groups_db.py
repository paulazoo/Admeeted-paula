import firebase_admin, datetime, math
import pandas as pd
from firebase_admin import credentials
from firebase_admin import firestore
from classes import User
from config import ExcelParser

cred = credentials.Certificate("./admeet2024privatekey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#%%
#get all the Albert Zhang users
user = db.collection(u'users').where(u'fullName', u'==', u'Albert Zhang')
user_stream=user.stream()
for i in user_stream:
    print('{} => {}\n'.format(i.id, i.to_dict()))


#%%
#get uhhhh this user by his user id
user_ref=db.collection(u'users').document('0JQunbpuKbcPpkA0hrN5')
user_ref.get()
user_ref.set({
    u'feedback': 'Horrible survey!'
}, merge=True)
    
#%%
##prints out all users
users_ref = db.collection(u'users')
docs = users_ref.stream()
for doc in docs:
    print(u'{} => {}\n'.format(doc.id, doc.to_dict()))



#Gets a specific document by id
# id = 'RFpaAfoQdqxXAMLQwBYj'
# doc_ref = db.collection('users').document(id)
#
# try:
#     doc = doc_ref.get()
#     print(u'Document data: {}'.format(doc.to_dict()))
# except google.cloud.exceptions.NotFound:
#     print(u'No such document!')

import firebase_admin, datetime, math
import pandas as pd
from firebase_admin import credentials
from firebase_admin import firestore
from classes import User
from config import ExcelParser

cred = credentials.Certificate("./admeet2024-firebase-adminsdk-oa4v1-1a11cd5d5a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


user_by_fullname = db.collection('users').where('fullName', u'==', 'Albert Zhang').stream()

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

import firebase_admin, datetime, math
import pandas as pd
from firebase_admin import credentials
from firebase_admin import firestore
from classes import User
from config import ExcelParser

cred = credentials.Certificate("./admeet-privatekey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def getYear(year):
    if year == "Prefrosh (if you're class of 2024)":
        return 2024
    elif year == "Junior":
        return 2021
    elif year == "Senior":
        return 2020
    else:
        raise NameError('The year %s was not recognized' % year)

def strToTuple(string):
    #Takes a comma seperated string and converts it to a tuple
    output = ()
    if string and string==string:
        output += tuple(str(string).split(", "))
    return output

def addNewUsers(usersList):
    #Upload all user objects in users list to the firestore database
    i=1
    total = len(usersList)
    for user in usersList:
        print("uploading %s out of %s" % (i, total))
        # print(user)
        db.collection('users').add(user.json())
        i+=1

#List of users
users = []

#Iterates through the spreadsheet rows and creates a list of user objects for Coke Scholars
myparser = ExcelParser("Coke_Scholars.xlsx")
for user in myparser.all_summary.iloc:
    users.append(User(user['Full Name'], user['Email Address'], 'Coke Scholars', user['Timestamp'], 2024, user['From'], strToTuple(user['Major']), (), strToTuple(user['Music']), strToTuple(user['Sports']), strToTuple(user['Hobbies']), user['Feedback :) '] if user['Feedback :) ']==user['Feedback :) '] else None))

#Iterates through the spreadsheet rows and creates a list of user objects for Harvard
myparser = ExcelParser("Harvard.xlsx")
for user in myparser.all_summary.iloc:
    users.append(User(user['Full Name'], user['Email Address'], 'Harvard', user['Timestamp'], 2024, user['From'], strToTuple(user['Major']), (), strToTuple(user['What genres of music do you like?']), strToTuple(user['What sports are you interested in?']), strToTuple(user['What are some of your interests or hobbies?']), user['Feedback :)'] if user['Feedback :)']==user['Feedback :)'] else None))

#Iterates through the spreadsheet rows and creates a list of user objects for Georgia Tech
myparser = ExcelParser("Georgia_Tech.xlsx")
for user in myparser.all_summary.iloc:
    users.append(User(user['Full Name'], user['Email Address'], 'Georgia Tech', user['Timestamp'], getYear(user['Grade / Class at College']), user['Where are you from?'], strToTuple(user['What do you want (or are considering) to major/concentrate in?']), (), strToTuple(user['What genres of music do you like?']), strToTuple(user['What sports are you interested in?']), strToTuple(user['What are some of your interests or hobbies?']), user['Feedback :) '] if user['Feedback :) ']==user['Feedback :) '] else None))

#Iterates through the spreadsheet rows and creates a list of user objects for MIT
myparser = ExcelParser("MIT.xlsx")
for user in myparser.all_summary.iloc:
    users.append(User(user['Full Name'], user['Email Address'], 'MIT', user['Timestamp'], getYear(user['Grade / Class at College']), user['Where are you from?'], strToTuple(user['What do you want (or are considering) to major/concentrate in?']), (), strToTuple(user['What genres of music do you like?']), strToTuple(user['What sports are you interested in?']), strToTuple(user['What are some of your interests or hobbies?']), user['Feedback :) '] if user['Feedback :) ']==user['Feedback :) '] else None))

#Iterates through the spreadsheet rows and creates a list of user objects for Stanford
myparser = ExcelParser("Stanford.xlsx")
for user in myparser.all_summary.iloc:
    users.append(User(user['Full Name'], user['Email Address'], 'Stanford', user['Timestamp'], getYear(user['Grade / Class at College']), user['Where are you from?'], strToTuple(user['What do you want (or are considering) to major/concentrate in?']), (), strToTuple(user['What genres of music do you like?']), strToTuple(user['What sports are you interested in?']), strToTuple(user['What are some of your interests or hobbies?']), user['Feedback :) '] if user['Feedback :) ']==user['Feedback :) '] else None))

#Iterates through the spreadsheet rows and creates a list of user objects for Princeton
myparser = ExcelParser("Princeton.xlsx")
for user in myparser.all_summary.iloc:
    users.append(User(user['Full Name'], user['Email Address'], 'Princeton', user['Timestamp'], getYear(user['Grade / Class at College']), user['Where are you from?'], strToTuple(user['What do you want (or are considering) to concentrate in?']), strToTuple(user['What do you want (or considering) to certificate in?']), strToTuple(user['What genres of music do you like?']), strToTuple(user['What sports are you interested in?']), strToTuple(user['What are some of your interests or hobbies?']), user['Feedback :)'] if user['Feedback :)']==user['Feedback :)'] else None))

addNewUsers(users)

print("done!")




#prints out all users
# users_ref = db.collection(u'users')
# docs = users_ref.stream()
# for doc in docs:
#     print(u'{} => {}\n'.format(doc.id, doc.to_dict()))



#Gets a specific document by id
# id = 'RFpaAfoQdqxXAMLQwBYj'
# doc_ref = db.collection('users').document(id)
#
# try:
#     doc = doc_ref.get()
#     print(u'Document data: {}'.format(doc.to_dict()))
# except google.cloud.exceptions.NotFound:
#     print(u'No such document!')

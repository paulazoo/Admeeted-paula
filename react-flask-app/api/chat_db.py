#%%
#some packages to import
#to install a package on python: pip install [package name]
from datetime import date, datetime
today=date.today()
now=datetime.now()
import time

import logging
import os
from db import get_db
db=get_db()

#internal imports

#%%
def new_msg_db(user_uid, msg, convo_uid):

    msgName=db.child("users").child(user_uid).child("displayName").get().val()
    if not msgName:
        msgName=db.child("users").child(user_uid).child("name").get().val()
    
    datestamp=today.strftime("%b-%d-%Y")
    timestamp=now.strftime("%H:%M:%S")
    
    msg_dict={
        'msgName':msgName,
        'datestamp':datestamp,
        'timestamp':timestamp,
        'msgtext':msg,
        'user':user_uid,
    }
    print(msg_dict)

    db.child("msg_convo").child(convo_uid).push(msg_dict)
    return

def get_msgs_db(convo_uid):

    msg_data=db.child("msg_convo").child(convo_uid).get().val()

    if msg_data:
        msg_data=list(msg_data.values())
    elif not msg_data:
        msg_data=[{}]
    return msg_data


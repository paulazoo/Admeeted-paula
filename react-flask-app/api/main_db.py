#some packages to import
#to install a package on python: pip install [package name]
from webbot import Browser
import pandas as pd
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import date
import time

import logging
import os
import threading


#internal imports
from api import firebase_db, helpers_db, groups_db
#import api.helpers_db
##group manipulations
#import api.groups_db

#%%
##inputs
#event_uid='Harvard Admeeted 2024 3-30'
#convo_name_str='Virtual Visitas 2.0'
#num_threads=3
    
#%%
def main_convos(event_uid, convo_name_str, num_threads):
    #who's logging
    current_user = os.getlogin()
    
    #format of log
    FORMAT='%(asctime)s:%(name)s:%(levelname)s:    %(message)s'
    #set up logging
    logging.basicConfig(format=FORMAT, filename='log_file2.log', level=logging.WARNING)
    
    #test the logger
    #new runs get a space in the log
    logging.warning('')
    #who started running?
    logging.warning('Log started with user: '+current_user)
    
    #%%
    #get event variables
    event_info=firebase_db.get_event_info(event_uid)
    
    #change depending on call type?
    all_users=firebase_db.get_org_users(event_info['org'], event_uid)
    
    #%%
    #user_email_dict=firebase_db.get_emails(all_users)
    user_email_dict=firebase_db.get_emails([])
    
    #%%
    #create groups using the createGroups function defined in groups.py file
    generated_groups = []
    
    for call_num in range(1, event_info['num_rounds'] + 1):
        generated_groups = generated_groups+groups_db.create_groups(list(user_email_dict.keys()), event_info['desired_size'], call_num)
    
    giant_dict = {}
    for i in range(len(generated_groups)):
        #unique convo_uid for firebase
        convo_uid = "%sCall%sGroup%d"%(event_uid, generated_groups[i][0], i)
        #actual displayName for google hangouts
        displayName = "%s Call %s"%(convo_name_str, generated_groups[i][0])
        #giant_dict with displayNames and corresponding emails
        giant_dict[convo_uid]={user_uid:user_email_dict[user_uid] for user_uid in generated_groups[i][1:] }
        #add displayName to each convo dict in giant_dict
        giant_dict[convo_uid].update({'displayName':displayName})
    
    
    logging.warning(giant_dict)
    
    #%%
    #back to firebase
    firebase_db.post_convo(giant_dict, event_uid, event_info)
    
    #%%
    #big dict with just the emails for threads
    big_dict={convo_uid:giant_dict[convo_uid]['displayName'] for convo_uid in giant_dict}
    
    #%%
    
    batched_dicts = helpers_db.split_dict(big_dict, num_threads)
    logging.warning("Batched dicts are:")
    logging.warning(batched_dicts)
    
    #%%
    thread_list=[]
    error_count = 0
    for batch in batched_dicts:
        try:
            t = threading.Thread(target=helpers_db.go_thread, args=(batch, batched_dicts.index(batch),))
            #starting thread
            t.start()
            #add thread to thread list
            thread_list.append(t)
        except:
            logging.warning("There was an error.")
            error_count += 1
    
    for t in thread_list:
        #join all the threads in thread_list
        t.join()
    # both threads completely executed 
    logging.warning("Done! There were " + str(error_count) + " errors.") 

#%%
    return
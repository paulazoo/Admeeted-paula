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
import firebase_db
import helpers_db
import groups_db
#import api.helpers_db
##group manipulations
#import api.groups_db

#%%
##inputs
#event_uid='Harvard Admeeted 2024 3-30'
#convo_name_str='Virtual Visitas 2.0'
#num_threads=3
    
#%%
def main_convos(event_uid, convo_name_str, num_threads, category=["random"]):
    #%%
    #set up logger
    #will not log unless basicConfig has been run outside of ipython console

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
    
    #%%
    '''
    delete this later
    '''
    category=category*event_info['num_rounds']
    #%%
    #create groups using the createGroups function defined in groups.py file
    generated_groups = []
    
    for call_num in range(1, event_info['num_rounds'] + 1):
        call_category=category[call_num-1]
        if call_category == 'major':
            all_users_all=firebase_db.get_major_users(event_info['org'],event_uid)
        elif call_category == 'random':
            all_users_all={'random':firebase_db.get_event_users(event_uid)}
        
        for all_users in all_users_all:
            #user_email_dict=firebase_db.get_emails(all_users)
            generated_groups = generated_groups+groups_db.create_groups(list(all_users_all[all_users]), event_info['desired_size'], call_num)

    print(f'Generated Groups: {generated_groups}')
#%%
    giant_dict = {}
    for i in range(len(generated_groups)):
        #unique convo_uid for firebase
        convo_uid = "%sCall%sGroup%d"%(event_uid, generated_groups[i][0], i)
        #actual displayName for google hangouts
        displayName = "%s Call %s"%(convo_name_str, generated_groups[i][0])
        #giant_dict with displayNames
        giant_dict[convo_uid]={user_uid:True for user_uid in generated_groups[i][1:] }
        #add displayName and category to each convo dict in giant_dict
        giant_dict[convo_uid].update({'displayName':displayName, 'category':category[int(generated_groups[i][0])-1]})
    
    logging.warning(giant_dict)
    
    #%%
    #back to firebase
    firebase_db.post_convo(giant_dict, event_uid, event_info)
    
#    #%%
#    #big dict with just the emails for threads
#     big_dict={convo_uid:giant_dict[convo_uid]['displayName'] for convo_uid in giant_dict}
#
#     #%%
#
#     batched_dicts = helpers_db.split_dict(big_dict, num_threads)
#     logging.warning("Batched dicts are:")
#     logging.warning(batched_dicts)
#
#     #%%
#     thread_list=[]
#     error_count = 0
#     for batch in batched_dicts:
#        try:
#            t = threading.Thread(target=helpers_db.go_thread, args=(batch, True, batched_dicts.index(batch),))
#            #starting thread
#            t.start()
#            #add thread to thread list
#            thread_list.append(t)
#        except:
#            logging.warning("There was an error.")
#            error_count += 1
#
#     for t in thread_list:
#        #join all the threads in thread_list
#        t.join()
#     # both threads completely executed
#     logging.warning("Done! There were " + str(error_count) + " errors.")
#
#     #%%
#     return

def empty_hangouts(name, num_hangouts, num_threads):
    thread_list = []
    error_count = 0
    empty_dict = {f'Convo {i}': name for i in range(num_hangouts)}
    batched_dicts = helpers_db.split_dict(empty_dict, num_threads)

    for batch in batched_dicts:
        print(f'Batch: {batch}')
        try:
            t = threading.Thread(target=helpers_db.go_thread, args=(batch, False, batched_dicts.index(batch),))
            # starting thread
            t.start()
            # add thread to thread list
            thread_list.append(t)
        except:
            logging.warning("There was an error.")
            error_count += 1

    for t in thread_list:
        # join all the threads in thread_list
        t.join()
        # both threads completely executed
    logging.warning("Done! There were " + str(error_count) + " errors.")
#some packages to import
#to install a package on python: pip install [package name]
from webbot import Browser
import pandas as pd
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import date
import hangout_tools
import time

#%%
#set up logger
#will not log unless basicConfig has been run outside of ipython console
import logging
import os

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
#inputs
event_uid='Harvard Admeeted 2024 3-30'

#%%
import firebase_db
#get event variables
displayName, num_rounds, desired_size, timeStart, org_uid=firebase_db.get_event_info(event_uid)
num_threads=int(input("num_threads? "))
#%%
#change depending on call type?
all_users=firebase_db.get_org_users(org_uid, event_uid)
all_emails=firebase_db.get_emails(all_users)


#%%
#group manipulations
import groups
#create groups using the createGroups function defined in groups.py file
generated_groups = []

for call_num in range(1, num_rounds + 1):
    #for each call, ask what category for the call
    #r for random
    category = input("category for call "+str(call_num)+"? ")

    #s for skip category combining
    generated_groups = generated_groups+groups.create_groups(all_emails, desired_size, call_num)

logging.warning(generated_groups)

#%%
#group name for hangout_tools
#make generated_groups into a dict
giant_dict = {}
for i in range(len(generated_groups)):
   group_name = "IGNORE TEST Call: %s %s %s PM EST Group number: %d"%(generated_groups[i][0], org_uid, timeStart, i)
   giant_dict[group_name]=generated_groups[i]

#%%
import helpers
import threading

batched_dicts = helpers.split_dict(giant_dict, num_threads)
logging.warning("Batched dicts are:")
logging.warning(batched_dicts)

#%%
thread_list=[]
error_count = 0
for batch in batched_dicts:
    try:
        t = threading.Thread(target=helpers.go_thread, args=(batch, batched_dicts.index(batch),))
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

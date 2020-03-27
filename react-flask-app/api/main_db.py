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
#initialize variables
#the config file cleans the data and gets the starting variable values
from config_db import MyParser

myparser = MyParser("Coke Scholars Virtual Visitas (Responses).xlsx")

myparser.desired
myparser.num_calls
myparser.num_threads

#%%
import firebase_db
all_emails=firebase_db.get_college_emails('Harvard')

#%%
#group manipulations
import groups
#create groups using the createGroups function defined in groups.py file
generated_groups = []
call_time = "3:00"
call_org = "Princeton 3/21"

for call_num in range(1, myparser.num_calls + 1):
    #for each call, ask what category for the call
    #r for random
    category = input("category for call "+str(call_num)+"? ")

    #s for skip category combining
    generated_groups = groups.make_call_groups(all_emails, myparser.desired, call_num, category, generated_groups)

logging.warning(generated_groups)
generated_groups_pd=pd.DataFrame(generated_groups)

#%%
#group name for hangout_tools
#make generated_groups into a dict
giant_dict = {}
for i in range(len(generated_groups)):
   group_name = "IGNORE TEST Call: %s %s %s PM EST Group number: %d"%(generated_groups[i][0], call_org, call_time, i)
   giant_dict[group_name]=generated_groups[i]

#%%
import helpers
import threading

batched_dicts = helpers.split_dict(giant_dict, myparser.num_threads)
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

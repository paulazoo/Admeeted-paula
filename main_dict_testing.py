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
from config import ExcelParser

myparser = ExcelParser("Princeton'ing for Quaran-teens (Responses) (1).xlsx")

myparser.all_summary
myparser.desired
myparser.all_emails
myparser.num_calls
myparser.num_threads

#%%
#group manipulations
import groups
#create groups using the createGroups function defined in groups.py file
generated_groups = []

for call_num in range(1, myparser.num_calls + 1):
    #for each call, ask what category for the call
    #r for random
    category = input("category for call "+str(call_num)+"? ")
    #s for skip category combining
    generated_groups = groups.make_call_groups(myparser.all_summary, myparser.all_emails, myparser.desired, call_num, category, generated_groups)

logging.warning(generated_groups)
generated_groups_pd=pd.DataFrame(generated_groups)

#%%
#group name for hangout_tools
#get the time to put into group_name later
generated_groups_pd['call_time']='3:00'
generated_groups_pd['group_num']=generated_groups_pd.index.astype(str)
generated_groups_pd["group_name"] = "Call: "+generated_groups_pd[0]+" Princeton 3/21 "+generated_groups_pd['call_time']+" PM EST Group number: " + generated_groups_pd['group_num']

#%%
import helpers
import threading

batched_lists = helpers.split_list(generated_groups, myparser.num_threads)
logging.warning("Batched lists are:")
logging.warning(batched_lists)

#%%
thread_list=[]
error_count = 0
for batch in batched_lists:
    try:
        t = threading.Thread(target=helpers.go_thread, args=(batch, batched_lists.index(batch),))
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

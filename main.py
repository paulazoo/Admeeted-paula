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

myparser = ExcelParser("Coke Scholars Virtual Visitas (Responses).xlsx")

myparser.all_summary
myparser.desired
myparser.all_emails
myparser.num_calls
myparser.num_threads

#%%
#group manipulations
import groups
#create groups using the createGroups function defined in groups.py file
all_generated_groups = []
call_time = "3:00"
call_org = "Princeton 3/21"

for call_num in range(1, myparser.num_calls + 1):
    #for each call, ask what category for the call
    category = input("category for call "+str(call_num)+"? ")
    #if category doesn't equal random
    if category != "r":
        #get by category groups
        by_category, category_strs=groups.get_category_random(myparser.all_summary, myparser.all_emails, category)
        
        #for groups too tiny
        tiny_groups = [group for group in by_category if len(group)<3]
        tiny_groups_strs = [category_strs[by_category.index(group)] for group in by_category if len(group)<=2]
        big_groups_strs = [category_val for category_val in category_strs if category_val not in tiny_groups_strs]

        print("")
        print("tiny groups: "+str(tiny_groups_strs))
        print("big groups: "+str(big_groups_strs))
        
        for tiny_group_idx, tiny_group in enumerate(tiny_groups):
            tiny_group_name=tiny_groups_strs[tiny_group_idx]
            add_to = input("Combine tiny group "+tiny_group_name+" to which group? ")
            #s to skip
            while (add_to not in category_strs) and (add_to != "s"):
                add_to = input(add_to+" is not a group. Combine tiny group "+tiny_group_name+" to which group? ")
            if add_to != "s":
                by_category[category_strs.index(add_to)]=by_category[category_strs.index(add_to)]+tiny_group
                by_category.pop(category_strs.index(tiny_group_name))
                category_strs.pop(category_strs.index(tiny_group_name))

        for i in range(0,len(category_strs)):
            #create_groups out of each by_category category value group
            #all groups with the same category have the same call
            all_generated_groups = all_generated_groups + groups.create_groups(by_category[i], myparser.desired, call_num)
    else:
        #for just random groups, run this
        all_generated_groups = all_generated_groups + groups.create_groups(myparser.all_emails, myparser.desired, call_num)

logging.warning(all_generated_groups)

#make all_generated_groups into a dict
giant_dict = {}
for i in range(len(all_generated_groups)):
   group_name = "Call: %s %s %s PM EST Group number: %d"%(all_generated_groups[i][0], call_org, call_time, i)
   giant_dict[group_name] = i

#%%
import helpers
import threading

batched_lists = helpers.split_dict(giant_dict, myparser.num_threads)
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

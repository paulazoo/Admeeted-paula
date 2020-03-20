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
logging.basicConfig(format=FORMAT, filename='log_file.log', level=logging.DEBUG)

#test the logger
#new runs get a space in the log
logging.info('')
#who started running?
logging.warning('Log started with user: '+current_user)

#%%
#initialize variables
#the config file cleans the data and gets the starting variable values
from config import ExcelParser

myparser = ExcelParser('Virtual Visitas (all Responses).xlsx')

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
        print("big groups: "+str(big_groups_strs))
        
        for tiny_group_idx, tiny_group in enumerate(tiny_groups):
            add_to = input("Add tiny group "+str(tiny_groups_strs[tiny_group_idx])+" to which big group? ")
            while add_to not in big_groups_strs:
                add_to = input("Not a big group. Add tiny group "+str(tiny_groups_strs[tiny_group_idx])+" to which big group? ")
            by_category[category_strs.index(add_to)]=by_category[category_strs.index(add_to)]+tiny_group
            
        
        for tiny_group, tiny_group_idx in enumerate(tiny_groups):
            add_to = input("add tiny group: "+tiny_groups_strs[tiny_group_idx]+" to which big group?")
            while add_to not in big_groups_strs:
                add_to = input("That's not a big group. Add tiny group: "+tiny_groups_strs[tiny_group_idx]+" to which big group?")
            group_idx=category_strs.index(add_to)
            by_category[group_idx]=by_category[group_idx]+tiny_group
                
            
                
        
        for i in range(0,len(category_strs)):
            #create_groups out of each by_category category value group
            #all groups with the same category have the same call
            
            all_generated_groups = all_generated_groups + groups.create_groups(by_category[i], myparser.desired, call_num)  
    else:
        #for just random groups, run this
        all_generated_groups = all_generated_groups + groups.create_groups(myparser.all_emails, myparser.desired, call_num)

logging.warning(all_generated_groups)

#%%
for i in range(1, myparser.num_calls+1):
    all_generated_groups = all_generated_groups + groups.create_groups(myparser.all_emails, myparser.desired, i)
    logging.warning("hi")
#print the generated groups to check
logging.warning(len(all_generated_groups[0]))
logging.warning(all_generated_groups)

#%%
import helpers
import threading

batched_lists = helpers.split_list(all_generated_groups, myparser.num_threads)
#batchedLists = splitList(batchedLists, num_threads)
logging.warning("Batched lists are:")
logging.warning(batched_lists)

#%%
print("yo")
time.sleep(5)

#%%
thread_list=[]
error_count = 0
for i in batched_lists:
    try:

        t = threading.Thread(target=helpers.go_thread, args=(i,batched_lists.index(i),))      
        # starting thread 1 
        t.start()
        thread_list.append(t)
        
    except:
        logging.warning("There was an error.")
        error_count += 1

for t in thread_list:
    t.join()
# both threads completely executed 
logging.warning("Done! There were " + str(error_count) + " errors.") 

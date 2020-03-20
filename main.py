#some packages to import
#to install a package on python: pip install [package name]
from webbot import Browser
import pandas as pd
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import date
import hangout_tools

#%%
import logging
#set up logger
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT, filename='log_file_name.txt')
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)

#%%
#initialize variables
#the config file cleans the data and gets the starting variable values
from config import ExcelParser

myparser = ExcelParser('Coke Scholars Virtual Visitas (Responses).xlsx')

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

category = input("category? ")
#if category doesn't equal random
if category != "Random":
    by_category, category_strs=groups.get_category_random(myparser.all_summary, myparser.all_emails, category)
    for i in range(0,len(category_strs)):
        all_generated_groups = all_generated_groups + groups.create_groups(by_category[i], myparser.desired, 1)
    
else:
    for call_num in range(0, myparser.num_calls):
        all_generated_groups = all_generated_groups + groups.create_groups(myparser.all_emails, myparser.desired, call_num)

for major in by_category:
    all_generated_groups = all_generated_groups + groups.create_groups(major, myparser.desired, 2)
    print(by_category.index(major))

print(all_generated_groups)

#%%
for i in range(1, myparser.num_calls+1):
    all_generated_groups = all_generated_groups + groups.create_groups(myparser.all_emails, myparser.desired, i)
    print("hi")
#print the generated groups to check
print(len(all_generated_groups[0]))
print(all_generated_groups)

#%%
import helpers
import threading

batched_lists = helpers.split_list(all_generated_groups, myparser.num_threads)
#batchedLists = splitList(batchedLists, num_threads)
print("Batched lists are:")
print(batched_lists)

#%%
thread_list=[]
error_count = 0
for batched_list in batched_lists:
    try:
        t = threading.Thread(target=helpers.go_thread, args=(batched_list,batched_lists.index(batched_list),))      
        # starting each thread
        t.start()
        #list of all threads
        thread_list.append(t)
        
    except:
        print("There was an error.")
        error_count += 1

for t in thread_list:
    #join all threads together
    t.join()
# both threads completely executed 
print("Done! There were " + str(error_count) + " errors.") 



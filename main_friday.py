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
start_time = time.time()


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
for call_num in range(0,myparser.num_calls):
    all_generated_groups = all_generated_groups + groups.create_groups(myparser.all_emails, myparser.desired, call_num)

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
for i in batched_lists:
    try:

        t = threading.Thread(target=helpers.go_thread, args=(i,batched_lists.index(i),))      
        # starting thread 1 
        t.start()
        thread_list.append(t)
        
    except:
        print("There was an error.")
        error_count += 1

for t in thread_list:
    t.join()
# both threads completely executed 
print("Done! There were " + str(error_count) + " errors.") 

time_to_run = time.time() - start_time
print("The program finished running in --- %s seconds ---" % (time_to_run))
print("The program finished running in " + str(time_to_run/60) + " minutes.")
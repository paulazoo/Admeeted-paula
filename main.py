#This was based on the main_v10_threading.py file. 
#some packages to import
#to install a package on python: pip install [package name]
from webbot import Browser
import pandas as pd
import time
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import date
import hangout_tools
#%%
#initialize variables
#the config file cleans the data and gets the starting variable values
import config_all as config
config.init('Testers Virtual Visitas (Responses).xlsx')
#get variables from config variables
All_Summary=config.All_Summary
desired=config.desired
allEmails=config.allEmails

#%%
#group manipulations
import groups
category = input("category? ")
if category != "Random":
    by_category, category_strs=groups.get_category_random(All_Summary, allEmails, category)

#%%
numCalls = int(input("How many times do you want people to call? "))

numThreads = int(input("How many threads/tabs/windows do you want to use? More means the program runs faster but takes more memory. "))

#%%
#create groups using the createGroups function defined in groups.py file
allGeneratedGroups = []

#allGeneratedGroups = allGeneratedGroups + groups.createGroups(allEmails, desired, 1)

for major in by_category:
    allGeneratedGroups = allGeneratedGroups + groups.createGroups(major, desired, 2)
    print(by_category.index(major))
#%%
print(allGeneratedGroups)
#%%
for i in range(1, numCalls+1):
    allGeneratedGroups = allGeneratedGroups + groups.createGroups(allEmails, desired, i)
    print("hi")
#print the generated groups to check
print(len(allGeneratedGroups[0]))
print(allGeneratedGroups)

#%%
import helpers
#define waitTime1 to prevent errors?
waitTime1 = 2
#get the date to put into groupName later
today = date.today()
dateNow = today.strftime("%B %d, %Y")
callTime = '9:30 PM EST'
category='Testing'
    
#%%
import threading
# creating thread 
catchErrors = True

batchedLists = helpers.splitList(allGeneratedGroups, numThreads)
#batchedLists = splitList(batchedLists, numThreads)
print("Batched lists are:")
print(batchedLists)


#%%
thread_list=[]
errorCount = 0
for i in batchedLists:
    try:

        t = threading.Thread(target=go_thread, args=(i,batchedLists.index(i),))      
        # starting thread 1 
        t.start()
        thread_list.append(t)
        
    except:
        print("There was an error.")
        errorCount += 1

for t in thread_list:
    t.join()
# both threads completely executed 
print("Done! There were " + str(errorCount) + " errors.") 



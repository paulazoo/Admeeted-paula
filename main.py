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
from config import ExcelParser

myparser = ExcelParser('Testers Virtual Visitas (Responses).xlsx')

myparser.all_summary
myparser.desired
myparser.all_emails
myparser.numCalls
myparser.numThreads
#%%
#group manipulations
import groups
category = input("category? ")
#if category doesn't equal random
if category != "Random":
    by_category, category_strs=groups.get_category_random(myparser.all_summary, myparser.all_emails, category)
    
#create groups using the createGroups function defined in groups.py file
allGeneratedGroups = []

allGeneratedGroups = allGeneratedGroups + groups.createGroups(myparser.all_emails, myparser.desired, 1)

for major in by_category:
    allGeneratedGroups = allGeneratedGroups + groups.createGroups(major, myparser.desired, 2)
    print(by_category.index(major))

print(allGeneratedGroups)
#%%
for i in range(1, myparser.numCalls+1):
    allGeneratedGroups = allGeneratedGroups + groups.createGroups(myparser.all_emails, myparser.desired, i)
    print("hi")
#print the generated groups to check
print(len(allGeneratedGroups[0]))
print(allGeneratedGroups)

#%%
import helpers
import threading
# creating thread 
catchErrors = True

batchedLists = helpers.splitList(allGeneratedGroups, myparser.numThreads)
#batchedLists = splitList(batchedLists, numThreads)
print("Batched lists are:")
print(batchedLists)

#%%
thread_list=[]
errorCount = 0
for i in batchedLists:
    try:

        t = threading.Thread(target=helpers.go_thread, args=(i,batchedLists.index(i),))      
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



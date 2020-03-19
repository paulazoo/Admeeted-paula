#some packages to import
#to install a package on python: pip install [package name]
#if people fill out the form after the groups are already made, just run this program again but only on the people who just joined, so go make a different excel with just the new emails and run it on that.
from webbot import Browser
import pandas as pd
import random
import time
import selenium
from selenium.common.exceptions import NoSuchElementException
from datetime import date
import keyboard

#%%
#initialize variables
#the config file cleans the data and gets the starting variable values
import config_all as config
config.init('Virtual Visitas (Responses) (2).xlsx')
#get variables from config variables
All_Summary=config.All_Summary
desired=config.desired
allEmailsNoDuplicates=config.allEmailsNoDuplicates

#%%
#group manipulations
import groups
numCalls = int(input("How many times do you want people to call? "))
#create groups using the createGroups function defined in groups.py file
allGeneratedGroups = []
for i in range(numCalls):
    allGeneratedGroups.append(groups.createGroups(allEmailsNoDuplicates, desired))
#print the generated groups to check
print(allGeneratedGroups)
print(str(len(allGeneratedGroups[0][0])))

#%%
#login file
import logging_in
#WaitTime is used with time.sleep() to make sure webpages are loading.
waitTime1 = 1
#login using the login function in logging_in.py
web=logging_in.login(waitTime1)

#%%
#initialize some variables
totalGroups = 0
#first call is callNum = 1
callNum = 1
#groupNum is just for our tracking purposes
groupNum = 1
#get the date to put into groupName later
today = date.today()
dateNow = today.strftime("%B %d, %Y")

#%%
#get out of iframe for making groups
web.driver.switch_to.default_content()

#make the number of generatedGroups corresponding to the number of calls
for generatedGroups in allGeneratedGroups:
    #start creating the hangout for each group in the generatedGroups for each designated call
    groupNum = 1
    for subGroup in generatedGroups:
        #groupName using the date and groupNum
        #groupName = dateNow + " Call " + str(groupNum) + " Key: "
        #Alternatively, make the groupName with the specific call time
        groupName = "March 15 9:30 PM EST," + " Call " + str(callNum)
        #hangout is not created yet
        notWorked = True
        while notWorked:
            #num = 8 is message, 7 is phone call, 6 is video call with tag = 'span', classname="Ce1Y1c"
            time.sleep(waitTime1)
            #click the message button in hangouts
            web.click(tag = 'span', classname="Ce1Y1c", number=8)
            web.click(tag = 'input', classname="tF")
            #skip to the entering group people box
            web.type("please work    " + "\t")

            web.press(web.Key.ENTER)
            
            #find the iframe for the box for creating hangouts
            iframe_pls=web.driver.find_element_by_xpath("//iframe[@class='Xyqxtc']")
            #get that iframe's id as a string
            iframe_id=iframe_pls.get_attribute("id")
            print(iframe_id)
            #get this correct iframe from it's id
            iframe_correct=web.driver.find_element_by_id(iframe_id)
            time.sleep(waitTime1)
            
            #switch to the correct iframe
            web.driver.switch_to.frame(iframe_correct)
            
            #enter all the emails
            for email in subGroup:
                #type the email string
                web.type(email)
                time.sleep(waitTime1*2)
                #cick the email to add
                try:
                    #for gmails click the gmail
                    element=web.driver.find_element_by_xpath("//li[@class='eh XcEgrf fp pu hy']").click()
                    print(email + " added")
                except NoSuchElementException:
                    #for non-gmails?? click the non gmails
                    print("No element found. Trying again...")
                    element=web.driver.find_element_by_xpath("//li[@class='eh XcEgrf fp pu hy c-P-p lebsnd Tb']").click()
                time.sleep(waitTime1)
                # except:
                #   print(email + " was not added.")
                #   #print(email)
                #   #print(str(len(email)))
                #   for i in range(len(email)): 
                #     keyboard.press_and_release('backspace')
                #     # time.sleep(0.5)
                #     # web.
                #     # print(str(i))
                time.sleep(waitTime1)
                
            #name the group input box
            web.driver.find_element_by_xpath("//input[@class='t0ZFWd AKyIEc ea-Ga-ea']").send_keys(groupName)
            time.sleep(waitTime1)
            #click green button to make group
            web.driver.find_element_by_xpath("//button[@class='PD7XNe yt1Zfc']").click()
            time.sleep(waitTime1)
            #get out of iframe for making groups
            web.driver.switch_to.default_content()
            #type and enter group introduction messages
            time.sleep(waitTime1*2)
            web.type("Hello! Welcome to the group for " + str(groupName) + ". The first call (the group labeled call 1) starts at the time in the title, while the other calls will follow subsequently. For this group, please make this the " + str(callNum) + " call. At the designated start time, someone should initiate the call. In order for this to work as smoothly as possible, we need to coordinate our calling. Albert originally planned for each call to be 15 minutes, but times will be flexible depending on how ya'll like the lengths, so please check the GroupMe for the official lengths for each call! You can always return to this chat later if ya'll want to talk more :) . Additionally, if you would like to leave early, just leave the groups that you won't be able to call in. So, you could choose to only partake in calls 1 to 3 if you prefer, but we all would love if you join all the calls. :D Thanks for helping make this happen!")
            #web.type("Hello! This is the testing for a program. Please ignore this hangout. You may exit.")
            time.sleep(waitTime1)
            web.press(web.Key.ENTER)
            
            #check if the group hangout was successfully created by checking if we're still in hangouts
            if 'hangouts.google.com' in web.get_current_url():
                #if we are, this hangout creation has worked
                notWorked = False
                #print that hangout group was successfully created
                print(groupName + " was successfully created, hopefully.")
                #total groups successfully created
                totalGroups += 1
            else:
                #didn't work, print that hangout was not successfully created
                print(groupName + " NOT successfully created.")
            time.sleep(waitTime1)
            #refresh the webpage to get back to general page for creating hangouts
            web.refresh()
        #move on to the next group
        #finished!
        print("The " + str(groupNum) + " group of the " + str(callNum) + " call has worked! We got to the end of the line!")
        groupNum += 1
    callNum += 1
    
    
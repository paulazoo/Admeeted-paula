#some packages to import
#to install a package on python: pip install [package name]
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
import config_excel_into_email_list as config
#clean and get the starting variable values
config.init()
#get variables from config variables
All_Summary=config.All_Summary
desired=config.desired
allEmailsNoDuplicates=config.allEmailsNoDuplicates

#%%
#group manipulations
import groups
#create groups using the createGroups function defined in groups.py file
generatedGroups = groups.createGroups(allEmailsNoDuplicates, desired)
#print the generated groups to check
print(generatedGroups)
print(str(len(generatedGroups[0])))

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
#first group is groupNum1
groupNum = 1
#get the date to put into groupName later
today = date.today()
dateNow = today.strftime("%B %d, %Y")

#%%
#get out of iframe for making groups
web.driver.switch_to.default_content()

#start creating the hangout for each group
for subGroup in generatedGroups:
    #groupName using the date and groupNum
    groupName = dateNow + " Call " + str(groupNum) + " Key: "
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
            try: 
                web.type(email)
                time.sleep(waitTime1*2)
                #cick the email to add
                #for gmails click the gmail
                element=web.driver.find_element_by_xpath("//li[@class='eh XcEgrf fp pu hy']").click()
                print(email + " added")
            #just delete the inputted email instead.
            #   except NoSuchElementException:
            #       #for non-gmails?? click the non gmails
            #       print("No element found. Trying again...")
            #       element=web.driver.find_element_by_xpath("//li[@class='eh XcEgrf fp pu hy c-P-p lebsnd Tb']").click()
            except:
              print(email + " was not added.")
              #print(email)
              #print(str(len(email)))
              for i in range(len(email)): 
                keyboard.press_and_release('backspace')
                # time.sleep(0.5)
                # web.press(web.Key.BACK_SPACE)
                # print(str(i))
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
        time.sleep(waitTime1)
        #web.type("Hello! Welcome to the group for " + groupName)
        web.type("Hello! This is the testing for a program. Please ignore this hangout. You may exit.")
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
    groupNum += 1
    #finished!
    print("The " + groupNum + " group has worked! We got to the end of the line!")
  
 
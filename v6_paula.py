from webbot import Browser
import pandas as pd
import random
import keyboard 
import time
import selenium
from selenium.common.exceptions import NoSuchElementException
import pyautogui 
from datetime import date


#get survey responses
excel_file = r'C:\Users\pkzr3\VirtualVisitas\Virtual Visitas (Responses).xlsx'
Summary = pd.read_excel(excel_file)
#%%
#initialize variables
import config
config.init()
All_Summary=config.All_Summary
desired=config.desired
allEmailsNoDuplicates=config.allEmailsNoDuplicates

#%%
#group manipulations
import groups
generatedGroups = groups.createGroups(allEmailsNoDuplicates, desired)

print(generatedGroups)
#%%
#login
import logging_in
#WaitTime is used with time.sleep() to make sure webpages are loading.
waitTime1 = 1
web=logging_in.login(waitTime1)

#%%

totalGroups = 0
notWorked = True
groupNum = 1
today = date.today()
dateNow = today.strftime("%B %d, %Y")


#%%
#get out of iframe for making groups
web.driver.switch_to.default_content()
        
for subGroup in generatedGroups:
    groupName = dateNow + " Call " + str(groupNum) + " Key: "
    notWorked = True
    while notWorked:
        #num = 8 is message, 7 is phone call, 6 is video call with tag = 'span', classname="Ce1Y1c"
        time.sleep(waitTime1)
        web.click(tag = 'span', classname="Ce1Y1c", number=8)
        web.click(tag = 'input', classname="tF")
        web.type("please work    " + "\t")
        web.press(web.Key.ENTER)
        
        #get into iframe
        iframe_pls=web.driver.find_element_by_xpath("//iframe[@class='Xyqxtc']")
        iframe_id=iframe_pls.get_attribute("id")
        print(iframe_id)
        iframe_correct=web.driver.find_element_by_id(iframe_id)
        'will this work? maybe.'
        time.sleep(waitTime1)
        web.driver.switch_to.frame(iframe_correct)
           
        for email in subGroup:
            #type the email string
            web.type(email)
            time.sleep(waitTime1*2)
            #cick the email to add
            try:
                #for gmails
                element=web.driver.find_element_by_xpath("//li[@class='eh XcEgrf fp pu hy']").click()
                print(email + " added")
            except NoSuchElementException:
                #for non-gmails??
                print("No element found. Trying again...")
                element=web.driver.find_element_by_xpath("//li[@class='eh XcEgrf fp pu hy c-P-p lebsnd Tb']").click()
            time.sleep(waitTime1)
            
        #name the group input box
        web.driver.find_element_by_xpath("//input[@class='t0ZFWd AKyIEc ea-Ga-ea']").send_keys(groupName)
        time.sleep(waitTime1)
        #click green button to make group
        web.driver.find_element_by_xpath("//button[@class='PD7XNe yt1Zfc']").click()
        time.sleep(waitTime1)
        #get out of iframe for making groups
        web.driver.switch_to.default_content()
        #introduce group
        time.sleep(waitTime1)
        web.type("Hello! Welcome to the group for " + groupName)
        time.sleep(waitTime1)
        web.press(web.Key.ENTER)
        
        if 'hangouts.google.com' in web.get_current_url():
            notWorked = False  
            print(groupName + " was successfully created, hopefully.")
            totalGroups += 1
        else:
            print(groupName + " NOT successfully created.")
        time.sleep(waitTime1)
        web.refresh()
    groupNum += 1
    print("it got to here! end of the browser")
  
      
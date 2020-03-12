from webbot import Browser
import pandas as pd
import random
import keyboard 
import time
import selenium
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
#starting browser and logging in to hangouts

#WaitTime is used with time.sleep() to make sure webpages are loading.
waitTime1 = 1

#start new browser
web = Browser()
time.sleep(waitTime1*2)
#go to hangouts
web.go_to('https://hangouts.google.com/')
web.maximize_window()
#sign in email
web.click('Sign in')
web.type('VirtualVisitas2.0' , into='Email')
web.click('NEXT' , tag='span')
time.sleep(waitTime1)
#sign in password
web.type('Apaar&AlbertSal' , into='Password' , id='passwordFieldId')
web.click('NEXT' , tag='span') # you are logged in . woohoooo
web.click('confirm')

#%%

totalGroups = 0
notWorked = True
groupNum = 1
today = date.today()
dateNow = today.strftime("%B %d, %Y")
groupName = dateNow + " Call " + str(groupNum) + " Key: "

#%%
for subGroup in generatedGroups:
    notWorked = True
    while notWorked:
        #num = 8 is message, 7 is phone call, 6 is video call with tag = 'span', classname="Ce1Y1c"
        time.sleep(waitTime1)
        web.click(tag = 'span', classname="Ce1Y1c", number=8)
        web.click(tag = 'input', classname="tF")
        web.type("please work    " + "\t")
        web.press(web.Key.ENTER)
        #%%
        #get into iframe
        iframe_pls=web.driver.find_element_by_xpath("//iframe[@class='Xyqxtc']")
        iframe_id=iframe_pls.get_attribute("id")
        iframe_correct=web.driver.find_element_by_id(iframe_id)
        'will this work? maybe.'
        web.driver.switch_to.frame(iframe_correct)
        #%%    
        for email in subGroup:
            #type the email string
            web.type(email)
            time.sleep(waitTime1)
            #cick the email to add
            time.sleep(waitTime1)
            web.driver.find_element_by_xpath("//li[@class='eh XcEgrf fp pu hy']").click()   
            
        #name the group input box
        web.driver.find_element_by_xpath("//input[@class='t0ZFWd AKyIEc ea-Ga-ea']").send_keys(groupName)
        time.sleep(waitTime1)
        #click green button to make group
        web.driver.find_element_by_xpath("//button[@class='PD7XNe yt1Zfc']").click()
        time.sleep(waitTime1)
        #get out of iframe for making groups
        web.driver.switch_to.default_content()
        #introduce group
        time.slee(waitTime1)
        web.type("Hello! Welcome to the group for " + groupName)
        time.sleep(waitTime1)
        web.press(web.Key.ENTER)
        #%%
        if 'hangouts.google.com' in web.get_current_url():
            notWorked = False  
            print(groupName + " was successfully created, hopefully.")
            totalGroups += 1
        else:
            print(groupName + " NOT successfully created.")
        time.sleep(waitTime1)
        time.sleep(waitTime1)
        web.refresh()
    groupNum += 1
    print("it got to here! end of the browser")
  
      
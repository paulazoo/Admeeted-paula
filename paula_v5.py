"""
For this to work, your display needs to be at the 1080p resolution with nothing obscuring the top left corner (so the task bar in Windows should be on the right or bottom, not top or left)
"""


from webbot import Browser
import pandas as pd
import random
import keyboard 
import time
import selenium
import pyautogui 
from datetime import date



excel_file = r'C:\Users\pkzr3\VirtualVisitas\Virtual Visitas (Responses).xlsx'
Summary = pd.read_excel(excel_file)
#%%
import config
config.init()
All_Summary=config.All_Summary
desired=config.desired
allEmailsNoDuplicates=config.allEmailsNoDuplicates

import groups
generatedGroups = groups.createGroups(allEmailsNoDuplicates, desired)

print(generatedGroups)
#%%
#WaitTime is used with time.sleep() to make sure webpages are loading. Especially for pyautogui
waitTime1 = 1


web = Browser()
time.sleep(waitTime1*2)
web.go_to('https://hangouts.google.com/')
web.maximize_window()
#for some reason going directly to hangouts.google.com doesn't work
web.click('Sign in')
web.type('VirtualVisitas2.0' , into='Email')
web.click('NEXT' , tag='span')
#For some reason this needs to be put twice to work
time.sleep(waitTime1)
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

        for email in subGroup:
            web.type(email)
            #pixel coordinates: x=260, y=395 on a 1080p screen. Just double the values for 4K. 
            time.sleep(waitTime1)
            #increase the second number if you're adding a lot of people to the gruop
            iframe_pls=web.driver.find_element_by_xpath("//iframe[@class='Xyqxtc']")
            iframe_id=iframe_pls.get_attribute("id")
            iframe_correct=web.driver.find_element_by_id(iframe_id)
            #%%
            'will this work? maybe.'
            web.driver.switch_to.frame(iframe_correct)
            
            #%%
            #cick the email to add
            web.driver.find_element_by_xpath("//li[@class='eh XcEgrf fp pu hy']").click()   
            #%%
        web.type("Hello! Welcome to the group for " + groupName, into = "Send a message", id=":9v.f")
        web.press(web.Key.ENTER)
        keyboard.write("Hello! Welcome to the group for " + groupName)
        keyboard.press("enter")
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
  
      
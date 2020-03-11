from webbot import Browser
import pandas as pd
import random
import keyboard 
import time
from selenium import webdriver
import pyautogui 
from datetime import date


#%%
import config
config.init()
allEmailsNoDuplicates=config.allEmailsNoDuplicates
desired=config.desired

#%%

def createGroups(allEmails, desired):
    # returns a list of the subgroups (which are also lists) of the emails.
    random.shuffle(allEmails)
    #desired = int(input("How many people would you like in a group: "))
    subgroups = [allEmails[x:x + desired] for x in range(0, len(allEmails), desired)]
    # if there's a group with less than desired number of people, evenly distribute amongst the other groups
    lastLen = len(subgroups[-1])
    if lastLen < desired:
        for x in range(lastLen):
            # if the remainder in the last group is larger than the number of subgroups, then it will add multiple people to the other groups.
            # Ex:
            subgroups[x % len(subgroups)].append(subgroups[-1][x])
            subgroups[-1][x] = 0

    subgroups = [x for x in subgroups if x != []]
    counter = 0
    for i in subgroups:
        for x in i:
            if x == 0:
                counter += 1
    if counter != 0:
        subgroups.pop(-1)
    return subgroups

#%%
def start_google_hangouts(waitTime1):
    
    web = Browser()
    '''
    Albert going directly to hangouts.google.com works for me?
    '''
    #this works tho
    web.go_to('https://hangouts.google.com/')
    web.maximize_window()
    
    #for some reason going directly to hangouts.google.com doesn't work
    #web.type('google hangouts online' + '\n')
    #web.click('hangouts.google.com')
    web.click('Sign in')
    web.type('VirtualVisitas2.0' , into='Email')
    web.click('NEXT' , tag='span')
    #For some reason this needs to be put twice to work
    time.sleep(waitTime1)
    web.type('Apaar&AlbertSal' , into='Password' , id='passwordFieldId')
    web.click('NEXT' , tag='span') # you are logged in . woohoooo
    web.click('confirm')
    return web

#%%
def make_hangouts(web,generatedGroups,waitTime1):
    totalGroups = 0
    
    groupNum = 1
    dateNow = date.today().strftime("%B %d, %Y")
    groupName = dateNow + " Call " + str(groupNum) + " Key: "
    
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
                web.type(email + '\t')
                #pixel coordinates: x=260, y=395 on a 1080p screen. Just double the values for 4K. 
                time.sleep(waitTime1)
                #increase the second number if you're adding a lot of people to the gruop
                for i in range(0,200,20):
                    pyautogui.click(260, 375+i)
                    #print("y = " + str(375+i)) 
                '''
                To Albert: iframe id seems to change every time login??
                '''
                iframe_id=web.driver.find_element_by_id("o6dv52z46ipg")
                
                web.driver.switch_to.frame(iframe_id)
                
                #tF gB Xp kG ea-Ga-ea input class according to inspect element
                web.driver.find_element_by_xpath("//input[@class='tF gB Xp kG ea-Ga-ea']").click()
                
                web.driver.switch_to.default_content()                
                '''
                '''
                for i in range(0,200,20):
                    pyautogui.click(460, 290+i)
            
            pyautogui.click(260, 230)
            whichCall = groupName + str(totalGroups);
            web.type(whichCall)
            pyautogui.click(440, 260)
            
            pyautogui.click(1450, 1060)
            pyautogui.click(1450, 1060)
            keyboard.write("Hello! Welcome to the group for " + groupName)
            keyboard.press("enter")
            if 'hangouts.google.com' in web.get_current_url():
                notWorked = False  
                print(groupName + " was successfully created, hopefully.")
                totalGroups += 1
            else:
                print(groupName + " NOT successfully created.")
            web.refresh()
        groupNum += 1
        print("it got to here! end of the browser")
        return web
    
#%%

# generate groups
generatedGroups = createGroups(allEmailsNoDuplicates, desired)
print(generatedGroups)

#WaitTime is used with time.sleep() to make sure webpages are loading. Especially for pyautogui
waitTime1 = 1
web=start_google_hangouts(waitTime1)

make_hangouts(web,generatedGroups,waitTime1)


      
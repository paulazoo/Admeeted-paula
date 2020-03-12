from webbot import Browser
import pandas as pd
import random
import keyboard 
import time
import selenium
import pyautogui 
from datetime import date

totalGroups = 0

excel_file = 'Virtual Visitas (Responses).xlsx'
Summary = pd.read_excel(excel_file)
#%%
# make sure the exact name of the column is Email
Summary = Summary["Email Address"]
Summary = Summary.dropna()
# Putting all the data into a pandas dataframe
desired = int(input("How many people would you like in a group? "))
allEmails1 = []
for i in Summary:
    allEmails1.append(i)
allEmailsNoDuplicates = list(dict.fromkeys(allEmails1))

# to test that all emails work
# print(allEmails1)
# allEmails now contains all of the emails from the Excel file with all NaN values dropped

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



    # then click a check mark

generatedGroups = createGroups(allEmailsNoDuplicates, desired)



print(generatedGroups)

notWorked = True
#WaitTime is used with time.sleep() to make sure webpages are loading. Especially for pyautogui
waitTime1 = 1
groupNum = 1
today = date.today()
dateNow = today.strftime("%B %d, %Y")
groupName = dateNow + " Call " + str(groupNum) + " Key: "
web = Browser()
web.go_to('google.com')
web.maximize_window()
#for some reason going directly to hangouts.google.com doesn't work
web.type('google hangouts online' + '\n')
web.click('hangouts.google.com')
web.click('Sign in')
web.type('VirtualVisitas2.0' , into='Email')
web.click('NEXT' , tag='span')
#For some reason this needs to be put twice to work
time.sleep(waitTime1)
web.type('Apaar&AlbertSal' , into='Password' , id='passwordFieldId')
web.type('Apaar&AlbertSal' , into='Password' , id='passwordFieldId')
web.click('NEXT' , tag='span') # you are logged in . woohoooo
web.click('confirm')


for subGroup in generatedGroups:
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
            #!!!!!!!!!!!!!!!!!!!!!!!

            #This is where we are stuck! Adding people to the hangout! because we can't do it with pyauto.gui since the location to add files is too small. :( . Probably need to inspect element this.

            #!!!!!!!!!!!!!!!!!
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
  
      
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
print("It's running")
#%%
#initialize variables
#the config file cleans the data and gets the starting variable values
import config_all as config
config.init("GT'ing for Quaran-teens (Responses) (2).xlsx")
#get variables from config variables
All_Summary=config.All_Summary
desired=config.desired
allEmailsNoDuplicates=config.allEmailsNoDuplicates

#%%
#group manipulations
import groups
numCalls = int(input("How many times do you want people to call? "))

numThreads = int(input("How many threads/tabs/windows do you want to use? More means the program runs faster but takes more memory. "))

#create groups using the createGroups function defined in groups.py file
allGeneratedGroups = []
for i in range(numCalls):
    allGeneratedGroups = allGeneratedGroups + groups.createGroups(allEmailsNoDuplicates, desired, i)
    print("hi")
#print the generated groups to check
print(len(allGeneratedGroups[0]))
print(allGeneratedGroups)

#%%

#define waitTime1 to prevent errors?
waitTime1 = 2

#%%
#starting browser and logging in to hangouts
def login(waitTime1):    
    #start new browser
    web = Browser()
    #go to hangouts
    web.driver.get('https://accounts.google.com/signin/v2/identifier?service=talk&passive=1209600&continue=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&followup=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    time.sleep(waitTime1)
    #sign in email
    web.driver.find_element_by_css_selector("input[type='email']").send_keys('VirtualVisitas3.0')
    web.driver.find_element_by_css_selector("input[type='email']").send_keys(Keys.RETURN)
    time.sleep(waitTime1)
    web.driver.find_element_by_css_selector("input[type='password']").send_keys('MyDeetYeet')
    web.driver.find_element_by_css_selector("input[type='password']").send_keys(Keys.RETURN)
    return web

#%%
def enter_email(web, email, groupName):
    #type the email string
    web.type(email)
    time.sleep(waitTime1)
    #cick the email to add
    try:
        #try to click any element that looks like it might be a clickable email
        element=web.driver.find_element_by_css_selector("li[class*='eh XcEgrf fp pu hy']").click()
    except NoSuchElementException:
        #still doesn't work? just move on
        print("skipping "+ str(email))
        with open("dropped_ppl.txt", "w") as outfile:
            #writes the call and groupNum, then the email that wasn't add to that hangout
            outfile.write("\n" + groupName + " " + email)
# except:
#   print(email + " was not added.")
#   #print(email)
#   #print(str(len(email)))
#   for i in range(len(email)): 
#     keyboard.press_and_release('backspace')
#     # time.sleep(0.5)
#     # web.
#     # print(str(i))
    return web

#%%
def create_hangout(web, subGroup, groupName, totalGroups, waitTime1):

        #write down the generatedGroups
    with open("group_ppl.txt", "a") as file:
        file.write("\n")
        file.write("groupName: "+groupName+" ppl: "+ str(subGroup))
    #Alternatively, make the groupName with the specific call time
    #groupName = "Testing, March 15 9:30 PM," + " Call " + str(callNum)
    #hangout is not created yet
    notWorked = True
    while notWorked:
        #num = 8 is message, 7 is phone call, 6 is video call with tag = 'span', classname="Ce1Y1c"
        #click the message button in hangouts
        web.click(tag = 'span', classname="Ce1Y1c", number=8)
        web.click(tag = 'input', classname="tF")
        #skip to the entering group people box
        web.type("\t")
        web.press(web.Key.ENTER)
        
        #find the iframe for the box for creating hangouts
        iframe_pls=web.driver.find_elements_by_css_selector("iframe[aria-label=\"Contacts and conversations\"]")
        #get that iframe's id as a string
        iframe_id=iframe_pls[0].get_attribute("id")
        #get this correct iframe from it's id
        iframe_correct=web.driver.find_element_by_id(iframe_id)
        
        #switch to the correct iframe
        web.driver.switch_to.frame(iframe_correct)
        
        #enter all the emails
        for i in range(1, len(subGroup)):
            print(subGroup[i])
            enter_email(web, subGroup[i], groupName)
            
            
        #name the group input box
        web.driver.find_element_by_css_selector("input.t0ZFWd.AKyIEc.ea-Ga-ea").send_keys(groupName)
        time.sleep(waitTime1)
        #click green button to make group
        web.driver.find_element_by_css_selector("button.PD7XNe.yt1Zfc").click()
        #get out of iframe for making groups
        web.driver.switch_to.default_content()
        time.sleep(waitTime1)
        #type and enter group introduction messages
        web.type("Hello! Welcome to the group for " + str(groupName) + ". Please make this the designated call (from the title). At the designated start time, someone should initiate the call. In order for this to work as smoothly as possible, we need to coordinate our calling. Albert originally planned for each call to be 30 minutes, with 3 calls in total, but times will be flexible depending on how ya'll like the lengths, so please check the GroupMe for the official lengths for each call! You can always return to this chat later if ya'll want to talk more :) . Additionally, if you would like to leave early, just leave the groups that you won't be able to call in. So, you could choose to only partake in calls 1 to 3 if you prefer, but we all would love if you join all the calls. :D Thanks for helping make this happen! --------------------------------------------------- ---------------------------------------------- ------------------------------------------------------------------Icebreakers (Questions) to spice up the conversation! Two truths and a lie What is your favorite high school memory? What is your most used emoji? You have your own late night talk show, who would you invite as your first guest? You have to sing karaoke, what song do you pick? What’s your life’s theme song? What’s the best piece of advice you’ve ever given? What is your absolute dream job? If you had to delete all but 3 apps on your smartphone, which ones would you keep? Coffee or tea? What is your cellphone wallpaper?")
        #web.type("Hello! This is the testing for a program. Please ignore this hangout. You may exit.")
        time.sleep(waitTime1)
        web.press(web.Key.ENTER)
        
        #check if the group hangout was successfully created by checking if we're still in hangouts
        #if 'hangouts.google.com' in web.get_current_url():
        #    #if we are, this hangout creation has worked
        #    notWorked = False
        #    #print that hangout group was successfully created
        #    print(groupName + " was successfully created, hopefully.")
        #    #total groups successfully created
        #    totalGroups += 1
        #else:
        #    #didn't work, print that hangout was not successfully created
        #    print(groupName + " NOT successfully created.")
        
        #exit out of the group hangout
            #get into iframe
        iframe_pls=web.driver.find_elements_by_css_selector("iframe[aria-label='"+groupName+"']")
        iframe_id=iframe_pls[0].get_attribute("id")
        iframe_correct=web.driver.find_element_by_id(iframe_id)
        web.driver.switch_to.frame(iframe_correct)
        
        #click to exist specific hangout iframe
        web.driver.find_element_by_css_selector("button.gGnOIc.tV.qp.SD.p7oPo.JPiKic").click()    
        
        #get out of specific group hangout iframe
        web.driver.switch_to.default_content()
        time.sleep(waitTime1)
        
        return web, totalGroups
#%%
def go_thread(givenGroups, threadNum):
    #WaitTime is used with time.sleep() to make sure webpages are loading.
    waitTime1 = 2
    #initialize some variables
    totalGroups = 0
    #groupNum is just for our tracking purposes
    groupNum = 1
    #get the date to put into groupName later
    today = date.today()
    dateNow = today.strftime("%B %d, %Y")
    callTime = '9:30 PM EST'
    category='Testing'

    #login using the login function in logging_in.py
    web=login(waitTime1)
    print("Login worked")
    
    #get out of iframe for making groups
    web.driver.switch_to.default_content()
    time.sleep(waitTime1)
    

    #start creating the hangout for each group in the generatedGroups for each designated call
    groupNum = 1
    for subGroup in givenGroups:
        #groupName using the date and groupNum
        #groupName = dateNow + callTime + " Call " + str(callNum) + " (Key: " + category + str(callNum) + str(groupNum) + ")"
        #groupName="test t: "+str(threadNum) + " c: "+ str(subGroup[0]) + " g: "+str(groupNum)
        #groupName="First call 3/20/2020 3:00 EST: Call number: "+ str(subGroup[0] + 1)
        groupName="First call GT 3/20/2020 3:00 EST"
        web, totalGroups=create_hangout(web, subGroup, groupName, totalGroups,waitTime1)
        print(groupName)
        #web, totalGroups=create_hangout(web, subGroup, groupName, totalGroups,waitTime1)
        #move on to the next group
        #finished!
        print(str(groupName) +" created!")
        groupNum += 1

#%%
def splitList(seq, num): #input a list and the desired number of smaller lists. Returns a nested list with the smaller lists.
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    
    return out

#%%
import threading
# creating thread 
catchErrors = True

batchedLists = splitList(allGeneratedGroups, numThreads)
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



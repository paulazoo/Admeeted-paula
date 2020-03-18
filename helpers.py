#This was based on the main_v10_threading.py file. 
#some packages to import
#to install a package on python: pip install [package name]
from webbot import Browser
import time
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import date

#%%
#starting browser and logging in to hangouts
def login(waitTime1):    
    #start new browser
    web = Browser()
    #go to hangouts
    web.driver.get('https://accounts.google.com/signin/v2/identifier?service=talk&passive=1209600&continue=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&followup=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    time.sleep(waitTime1)
    #sign in email
    web.driver.find_element_by_css_selector("input[type='email']").send_keys('VirtualVisitas2.0')
    web.driver.find_element_by_css_selector("input[type='email']").send_keys(Keys.RETURN)
    time.sleep(waitTime1)
    web.driver.find_element_by_css_selector("input[type='password']").send_keys('Apaar&AlbertSal')
    web.driver.find_element_by_css_selector("input[type='password']").send_keys(Keys.RETURN)
    return web

#%%
def enter_email(web, email, groupName, waitTime1):
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
        web.type("Hello! Welcome to the group for " + str(groupName) + ". Please make this the designated call (from the title). At the designated start time, someone should initiate the call. In order for this to work as smoothly as possible, we need to coordinate our calling. Albert originally planned for each call to be 15 minutes, but times will be flexible depending on how ya'll like the lengths, so please check the GroupMe for the official lengths for each call! You can always return to this chat later if ya'll want to talk more :) . Additionally, if you would like to leave early, just leave the groups that you won't be able to call in. So, you could choose to only partake in calls 1 to 3 if you prefer, but we all would love if you join all the calls. :D Thanks for helping make this happen!")
        #web.type("Hello! This is the testing for a program. Please ignore this hangout. You may exit.")
        time.sleep(waitTime1)
        web.press(web.Key.ENTER)
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
        groupName="3/18/2020 3:00 EST: Call number: "+ str(subGroup[0] + 1)
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


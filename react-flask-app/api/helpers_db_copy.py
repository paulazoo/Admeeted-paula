# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:38:13 2020

@author: pkzr3
"""

#some packages to import
#to install a package on python: pip install [package name]
from webbot import Browser
import time
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import date
import logging

#internal imports
from firebase_db import post_convo_link
#%%
#starting browser and logging in to hangouts
def login(wait_time):    
    #start new browser
    web = Browser()
    # options = web.driver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors') 
    # options.add_argument('--ignore-ssl-errors')
    # web = web.driver.Chrome(chrome_options=options)
    #options = web.driver.ChromeOptions('--ignore-certificate-errors', '--ignore-ssl-errors')
    #go to hangouts
    web.driver.get('https://accounts.google.com/signin/v2/identifier?service=talk&passive=1209600&continue=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&followup=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    time.sleep(wait_time*2)
    #sign in email
    web.driver.find_element_by_css_selector("input[type='email']").send_keys('VirtualVisitas4.0')
    web.driver.find_element_by_css_selector("input[type='email']").send_keys(Keys.RETURN)
    time.sleep(wait_time*2)
    
    #password enter
    web.driver.find_element_by_css_selector("input[type='password']").send_keys('MyDeetYeet')
    web.driver.find_element_by_css_selector("input[type='password']").send_keys(Keys.RETURN)
    return web

#%%
#def enter_email(web, email, group_name, wait_time):
#    #type the email string
#    web.type(email)
#    time.sleep(wait_time)
#    #cick the email to add
#    try:
#        #try to click any element that looks like it might be a clickable email
#        element=web.driver.find_element_by_css_selector("li[class*='eh XcEgrf fp pu hy']").click()
#    except NoSuchElementException:
#        #still doesn't work? just move on
#        logging.warning("skipping "+ str(email))
#        with open("dropped_ppl.txt", "w") as outfile:
#            #writes the call and groupNum, then the email that wasn't add to that hangout
#            outfile.write("\n" + group_name + " " + email)
#    return web

#%%
def create_hangout(web, convo_uid, group_name, wait_time):

        #write down the generatedGroups
    # with open("group_ppl.txt", "a") as file:
    #     file.write("\n")
    #     file.write("group_name: "+group_name+" ppl: "+ str(subgroup))
    #Alternatively, make the group_name with the specific call time
    #group_name = "Testing, March 15 9:30 PM," + " Call " + str(callNum)
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
        
#        #enter all the emails
#        for i in range(0, len(subgroup)-1):
#            #logging.warning(subgroup[i])
#            time.sleep(wait_time)
#            enter_email(web, subgroup[i], group_name, wait_time)
#            
        #name the group input box
        web.driver.find_element_by_css_selector("input.t0ZFWd.AKyIEc.ea-Ga-ea").send_keys(group_name)
        time.sleep(wait_time)
        #click green button to make group
        web.driver.find_element_by_css_selector("button.PD7XNe.yt1Zfc").click()
        #get out of iframe for making groups
        web.driver.switch_to.default_content()

        #get into iframe
        time.sleep(wait_time)
        iframe_pls=web.driver.find_elements_by_css_selector("iframe[aria-label='"+group_name+"']")
        iframe_id=iframe_pls[0].get_attribute("id")
        iframe_correct=web.driver.find_element_by_id(iframe_id)
        web.driver.switch_to.frame(iframe_correct)
        
        web.driver.find_element_by_css_selector("div[class='BB']").click()
        web.driver.find_elements_by_css_selector("button.wY.tR.bO4S5d.tJ.OzHnnb")[2].click()
        time.sleep(wait_time)
        link=web.driver.find_element_by_css_selector("input[class='LpmM1 iF0pUc']").get_attribute('value')
        #print('link: '+str(link))
        post_convo_link(convo_uid, link)
        #click to exist specific hangout iframe
        web.driver.find_element_by_css_selector("button.gGnOIc.tV.qp.SD.p7oPo.JPiKic").click()    
        
        #get out of specific group hangout iframe
        web.driver.switch_to.default_content()
        time.sleep(wait_time)
        
        return web
    
#%%
def go_thread(given_groups, thread_num):
    wait_time = 2
    
    #login using the login function in logging_in.py
    web=login(wait_time)
    logging.warning("Login worked")
    
    #get out of iframe for making groups
    web.driver.switch_to.default_content()
    time.sleep(wait_time)
    
    #start creating the hangout for each group in the generatedGroups for each designated call
    for convo_uid in given_groups:
        logging.warning("Now creating " + str(convo_uid))
        web = create_hangout(web, convo_uid, given_groups[convo_uid], wait_time)

        #web, total_groups=create_hangout(web, subgroup, group_name, total_groups,wait_time)
        #move on to the next group
        #finished!
        logging.warning(str(convo_uid) +" created!")


# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:02:49 2020

@author: pkzr3
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:54:24 2020

@author: pkzr3
"""
import logging
import time
from webbot import Browser
from helpers_db import login
from firebase_db import new_empty_hangout
#%%
def make_empty_hangouts(num_hangouts):
    wait_time=1
    #login using the login function in logging_in.py
    web=login(wait_time)
    logging.warning("Login worked")
    
    #get out of iframe for making groups
    web.driver.switch_to.default_content()
    time.sleep(wait_time)
    
    for i in range(0, num_hangouts):
        group_name='hangout'
        
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
        new_empty_hangout(link)
        #click to exist specific hangout iframe
        web.driver.find_element_by_css_selector("button.gGnOIc.tV.qp.SD.p7oPo.JPiKic").click()    
        
        #get out of specific group hangout iframe
        web.driver.switch_to.default_content()
        time.sleep(wait_time)


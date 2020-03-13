import time
from webbot import Browser

#%%
#open a specific group hangout
def open_group_hangout(web, groupName, waitTime1):
    #get out of any iframes
    web.driver.switch_to.default_content()
    
    #get into conversations iframe
    iframe_pls=web.driver.find_elements_by_xpath("//iframe[@aria-label='Contacts and conversations']")
    iframe_id=iframe_pls[0].get_attribute("id")
    iframe_correct=web.driver.find_element_by_id(iframe_id)
    time.sleep(waitTime1)
    web.driver.switch_to.frame(iframe_correct)
        
    #open specific group by groupName
    web.driver.find_element_by_css_selector("[title*='"+groupName+"']").click()   
    time.sleep(waitTime1)
    
    #get out of conversations iframe
    web.driver.switch_to.default_content()
    
    return web
#%%
#start a call for a group hangout (that has already been opened)
def call_group_hangout(web, groupName, waitTime1):
    #get out of any iframes
    web.driver.switch_to.default_content()
    
    #get into iframe
    iframe_pls=web.driver.find_elements_by_xpath("//iframe[@aria-label='" +groupName+ "']")
    iframe_id=iframe_pls[0].get_attribute("id")
    iframe_correct=web.driver.find_element_by_id(iframe_id)
    time.sleep(waitTime1)
    web.driver.switch_to.frame(iframe_correct) 
    
    #click video call
    web.driver.find_element_by_css_selector("[title*='Video call. Click to start a video call.']").click() 
    time.sleep(waitTime1*3)
    
    #get out of groupName specific hagnout iframe
    web.driver.switch_to.default_content()
    
    return web
    
#%%
#exit an already open group hangout
def exit_group_hangout(web, groupName, waitTime1):
    #get out of any iframes
    web.driver.switch_to.default_content()
    
    # #get into iframe
    iframe_pls=web.driver.find_elements_by_xpath("//iframe[@aria-label='" +groupName+ "']")
    iframe_id=iframe_pls[0].get_attribute("id")
    iframe_correct=web.driver.find_element_by_id(iframe_id)
    time.sleep(waitTime1)
    web.driver.switch_to.frame(iframe_correct) 
    
    #click to exist specific hangout iframe
    web.driver.find_element_by_xpath("//button[@class='gGnOIc tV qp SD p7oPo JPiKic']").click()    
    
    #get out of specific group hangout iframe
    web.driver.switch_to.default_content()
    
    return web

#%%
#write in an already open group hangout
#message is a string
def write_in_group_hangout(web, groupName, waitTime1, message):
    #get out of any iframes
    web.driver.switch_to.default_content()
    
    # #get into iframe
    iframe_pls=web.driver.find_elements_by_xpath("//iframe[@aria-label='" +groupName+ "']")
    iframe_id=iframe_pls[0].get_attribute("id")
    iframe_correct=web.driver.find_element_by_id(iframe_id)
    time.sleep(waitTime1)
    web.driver.switch_to.frame(iframe_correct) 
    
    #click hangout text input box
    web.driver.find_element_by_xpath("//div[@class='vE dQ editable']").click()
    #type in message string
    web.type(message)
    time.sleep(waitTime1)
    #enter message into hangout groupchat
    web.press(web.Key.ENTER)
    time.sleep(waitTime1)
    
    #get out of specific group hangout iframe
    web.driver.switch_to.default_content()
    
    return web

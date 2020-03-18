import time
from webbot import Browser
from selenium.common.exceptions import NoSuchElementException

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
    time.sleep(waitTime1)
    
    #get out of groupName specific hagnout iframe
    web.driver.switch_to.default_content()
    
    return web
    
#%%
#exit an already open group hangout
def exit_group_hangout(web, groupName, waitTime1):
    #get out of any iframes
    web.driver.switch_to.default_content()
    
    #get into iframe
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

#%%
#add a person to an existing already open group hangout
def add_to_group_hangout(web, groupName, waitTime1, email):
    #get out of any iframes
    web.driver.switch_to.default_content()
    
    #get into iframe
    iframe_pls=web.driver.find_elements_by_xpath("//iframe[@aria-label='" +groupName+ "']")
    iframe_id=iframe_pls[0].get_attribute("id")
    iframe_correct=web.driver.find_element_by_id(iframe_id)
    time.sleep(waitTime1)
    web.driver.switch_to.frame(iframe_correct) 
    
    #click hangout people button
    web.driver.find_element_by_xpath("//div[@class='dwrYTb PK']").click()
    #click Add people button
    web.click('Add people')
    #type the email string
    web.type(email)
    time.sleep(waitTime1*2)
    #cick the email to add
    try:
        #for gmails click the gmail
        element=web.driver.find_element_by_xpath("//li[@class='eh XcEgrf fp pu hy']").click()
        print(email + " added")
    except NoSuchElementException:
        #for non-gmails?? click the non gmails
        print("No element found. Trying again...")
        element=web.driver.find_element_by_xpath("//li[@class='eh XcEgrf fp pu hy c-P-p lebsnd Tb']").click()
    time.sleep(waitTime1)
    #click Add people button to finish adding
    web.click('Add people')
    
    #get out of specific group hangout iframe
    web.driver.switch_to.default_content()
    
    return web

#%%
def get_call_url(web,groupName,waitTime1):    
    #get into iframe
    iframe_pls=web.driver.find_elements_by_xpath("//iframe[@aria-label='" +groupName+ "']")
    iframe_id=iframe_pls[0].get_attribute("id")
    iframe_correct=web.driver.find_element_by_id(iframe_id)
    time.sleep(waitTime1)
    web.driver.switch_to.frame(iframe_correct) 
    
    #click video call
    web.driver.find_element_by_css_selector("button[title='Video call. Click to start a video call.']").click()
    
    #switch to video call
    web.driver.switch_to.window(web.driver.window_handles[1])
    #get call url
    call_url=web.get_current_url()
    #exit call
    element = web.driver.find_elements_by_css_selector("span[class='DPvwYc']")[2]
    web.driver.execute_script("arguments[0].click();", element)
    #switch back to original window
    web.driver.switch_to.window(web.driver.window_handles[0])
    #get back out of iframe
    web.driver.switch_to.default_content()
    return web, call_url
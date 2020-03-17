from webbot import Browser
import time
from selenium import webdriver

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
from webbot import Browser
import time
import selenium

#starting browser and logging in to hangouts
def login(waitTime1):    
    #start new browser
    web = Browser()
    time.sleep(waitTime1*2)
    #go to hangouts
    web.driver.get('https://accounts.google.com/signin/v2/identifier?service=talk&passive=1209600&continue=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&followup=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    #sign in email
    web.type('VirtualVisitas2.0' , into='Email')
    web.click('NEXT' , tag='span')
    #sign in password
    time.sleep(waitTime1)
    web.type('Apaar&AlbertSal' , into='Password' , id='passwordFieldId')
    web.click('NEXT' , tag='span') # you are logged in . woohoooo
    web.click('confirm')
    return web
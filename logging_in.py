from webbot import Browser
import time
import selenium

#starting browser and logging in to hangouts

def login(waitTime1):
    
    #start new browser
    web = Browser()
    time.sleep(waitTime1*2)
    #go to hangouts
    web.go_to('https://hangouts.google.com/')
    web.maximize_window()
    #sign in email
    web.click('Sign in')
    web.type('VirtualVisitas2.0' , into='Email')
    web.click('NEXT' , tag='span')
    time.sleep(waitTime1)
    #sign in password
    web.type('Apaar&AlbertSal' , into='Password' , id='passwordFieldId')
    web.click('NEXT' , tag='span') # you are logged in . woohoooo
    web.click('confirm')
    return web
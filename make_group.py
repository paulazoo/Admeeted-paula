# Make hangouts groups based on inputted list of emails.

from webbot import Browser
web = Browser()
web.go_to('google.com')
web.click('Sign in')
web.type('VirtualVisitas2.0' , into='Email')
web.click('NEXT' , tag='span')
#For some reason this needs to be put twice to work
web.type('Apaar&AlbertSal' , into='Password' , id='passwordFieldId')
web.type('Apaar&AlbertSal' , into='Password' , id='passwordFieldId')
web.click('NEXT' , tag='span') # you are logged in . woohoooo
web.click('confirm')
#for some reason going directly to hangouts.google.com doesn't work
web.go_to('google.com')
web.type('google hangouts' + '\n')
web.click('hangouts.google.com')
web.click('New conversation')
web.click('Izwf5d ptrgQb zv8lsd fTj9Ab')
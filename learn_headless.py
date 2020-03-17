#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
web = webdriver.Chrome(options=options)
#%%
web.get('https://accounts.google.com/signin/v2/identifier?service=talk&passive=1209600&continue=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&followup=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
#sign in email
web.find_element_by_css_selector("input[type='email']").send_keys('VirtualVisitas2.0')
web.find_element_by_css_selector("input[type='email']").send_keys(Keys.RETURN)

web.find_element_by_css_selector("input[type='password']").send_keys('Apaar&AlbertSal')
web.find_element_by_css_selector("input[type='password']").send_keys(Keys.RETURN)
web.get_screenshot_as_file('main-page.png')




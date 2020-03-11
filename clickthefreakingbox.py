#%%
#selenium
from selenium import webdriver
#keyboard manipulation
from selenium.webdriver.common.keys import Keys
#keep track of time
import time

#%%
#set email and password
email='paulakaitlynzoo@gmail.com'
password ='paula3.14'

#%%
#open webdriver chrome browser
driver = webdriver.Chrome(r'C:\Users\pkzr3\VirtualVisitas/chromedriver.exe')

#login page
time.sleep(5)
driver.get('https://accounts.google.com/servicelogin')

time.sleep(2)
'logging in...'
#email enter
driver.find_element_by_id('identifierId').send_keys(email)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

time.sleep(2)
#password
driver.find_element_by_css_selector("input[type=password]").send_keys(password)
time.sleep(5)
driver.find_element_by_id('passwordNext').click()
#time to load
time.sleep(2)
'logged in'
#%%
#i6zqysg3fczx
iframe_id=driver.find_element_by_id("z26yd6d8yta")
#%%
driver.switch_to.frame(iframe_id)

#%%
#tF gB Xp kG ea-Ga-ea
driver.find_element_by_xpath("//input[@class='tF gB Xp kG ea-Ga-ea']").click()
password = "DONT_YOU_DARE_STEAL_MY_PW!"
#I'm creating a new email and GroupMe account for this lol
#I'm thinking of naming it sambot but lmk if you want it to be
#something more official haha



























import pandas as pd 
import numpy as np
import time
import webbot
from webbot import Browser
from selenium.webdriver.common.keys import Keys
#print("hello world")
samantha_array = pd.Series(["hi", "thank", "you", "so", "much"])
print(type(samantha_array))
print(samantha_array)
web = Browser()
#web.driver.get("https://www.google.com")
web.driver.get("https://web.groupme.com/signin")
time.sleep(1)
web.driver.find_element_by_id("signinUserNameInput").send_keys("sammie7242@gmail.com")
web.driver.find_element_by_id("signinPasswordInput").send_keys(password)
web.driver.find_element_by_id("signinPassWordInput").send_keys(Keys.RETURN)

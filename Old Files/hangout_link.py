# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:49:38 2020

@author: pkzr3
"""
#%%
import helpers_db
web=helpers_db.login(2)
#%%
convo='NEW THIRD Call: 1 Harvard 3/26 3:00 PM EST Group number: 3'
web=open_group_hangout(web,convo,2)
#%%
import time
web.driver.find_element_by_css_selector("div[class='BB']").click()
web.driver.find_elements_by_css_selector("button.wY.tR.bO4S5d.tJ.OzHnnb")[2].click()
time.sleep(2)
link=web.driver.find_element_by_css_selector("input[class='LpmM1 iF0pUc']").get_attribute('value')
 



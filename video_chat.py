def call_group(web, groupName, waitTime1):
#%%
web.driver.switch_to.default_content()
groupName1='March 12, 2020 Call 1 Key: '
groupName2='March 12, 2020 Call 2 Key: '

#get into iframe
iframe_pls=web.driver.find_element_by_xpath("//iframe[@class='Xyqxtc']")
iframe_id=iframe_pls.get_attribute("id")
print(iframe_id)
iframe_correct=web.driver.find_element_by_id(iframe_id)
time.sleep(waitTime1)
web.driver.switch_to.frame(iframe_correct)
print('in iframe...')
#reopen specific group by groupName
web.driver.find_element_by_css_selector("[title*='"+groupName1+"']").click()   
time.sleep(1)
web.driver.switch_to.default_content()
#get into (2nd) iframe
iframe_pls=web.driver.find_elements_by_xpath("//iframe[@class='Xyqxtc']")

iframe_id=iframe_pls[1].get_attribute("id")
print(iframe_id)

iframe_correct=web.driver.find_element_by_id(iframe_id)
time.sleep(waitTime1)
web.driver.switch_to.frame(iframe_correct)
print('in iframe...')
web.driver.find_element_by_css_selector("[title*='Video call. Click to start a video call.']").click() 

#%%
web.driver.find_element_by_css_selector("[title*='"+groupName2+"']").click()   
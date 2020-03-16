#%%
import hangout_tools
web.driver.find_element_by_css_selector("[title*='Video call. Click to start a video call.']").click()
web.driver.switch_to.window(1)
print(web.get_current_url())
import pickle

#%%
def save_cookie(web, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(web.driver.get_cookies(), filehandler)

#%%
def load_cookie(web, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             web.driver.add_cookie(cookie)
             
#%%    
             
#start new browser
web = Browser()
# options = web.driver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors') 
# options.add_argument('--ignore-ssl-errors')
# web = web.driver.Chrome(chrome_options=options)
#options = web.driver.ChromeOptions('--ignore-certificate-errors', '--ignore-ssl-errors')
#go to hangouts
web.driver.get('https://accounts.google.com/signin/v2/identifier?service=talk&passive=1209600&continue=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&followup=https%3A%2F%2Fhangouts.google.com%2Fwebchat%2Fstart&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
time.sleep(wait_time*2)
#sign in email
web.driver.find_element_by_css_selector("input[type='email']").send_keys('VirtualVisitas4.0')
web.driver.find_element_by_css_selector("input[type='email']").send_keys(Keys.RETURN)
time.sleep(wait_time*2)

#password enter
web.driver.find_element_by_css_selector("input[type='password']").send_keys('MyDeetYeet')
web.driver.find_element_by_css_selector("input[type='password']").send_keys(Keys.RETURN)

#%%

save_cookie(web.driver, '/tmp/cookie')


#%%
#web.driver.find_element_by_css_selector("span[title='Official Harvard Online Class of 2024!']").click()
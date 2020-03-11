from webbot import Browser

#%%

def click_f_box(web):
    #z26yd6d8yta for paulakaitlynzoo@gmail.com
    #i6zqysg3fczx VirtualVisitas2.0
    '''
    To Albert: seems to change every time login??
    '''
    iframe_id=web.driver.find_element_by_id("o6dv52z46ipg")
    
    web.driver.switch_to.frame(iframe_id)
    
    #tF gB Xp kG ea-Ga-ea input class according to inspect element
    web.driver.find_element_by_xpath("//input[@class='tF gB Xp kG ea-Ga-ea']").click()
    
    web.driver.switch_to.default_content()
    
    return web
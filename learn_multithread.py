import threading

from webbot import Browser
import pandas as pd
import time
import selenium
from selenium.common.exceptions import NoSuchElementException
from datetime import date
import hangout_tools

import logging_in
t=1
#%%
  
def login1(waitTime1): 
    #login using the login function in logging_in.py
    logging_in.login(waitTime1)
    print("logged in 1")
    return web
  
def login2(waitTime1): 
    #login using the login function in logging_in.py
    logging_in.login(waitTime1)
    print("logged in 2")
    return web
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=login1, args=(t,)) 
    t2 = threading.Thread(target=login2, args=(t,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 

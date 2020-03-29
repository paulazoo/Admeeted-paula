#import pandas package for doing stuff with data
import pandas as pd
import os
import numpy
import logging

class MyParser():
    #define an initial function that when run, initializes variables
    def __init__(self, excel_name):
        #get current directory path on specific computer using os
        dir_path = os.path.dirname(os.path.realpath(excel_name))
        #file location for respones excel file
        excel_file = dir_path + "/" + excel_name
        logging.warning("file location at "+excel_file)
        #all_summary holds the survey response data as a pandas dataframe
        self.all_summary = pd.read_excel(excel_file)

        #desired for the desired number of ppl per group
        #self.desired = int(input("How many people would you like in a group? "))
        
        #number of total calls
        #self.num_calls = int(input("How many times do you want people to call? "))
        
        #number of total threads
        #self.num_threads = int(input("How many threads/tabs/windows do you want to use? More means the program runs faster but takes more memory. "))

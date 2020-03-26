#import pandas package for doing stuff with data
import pandas as pd
import os
import logging

class ExcelParser():
    #define an initial function that when run, initializes variables
    def __init__(self, excel_name):
        #get current directory path on specific computer using os
        dir_path = os.path.dirname(os.path.realpath(excel_name))
        #file location for respones excel file
        excel_file = dir_path + "/" + excel_name
        logging.warning("file location at "+excel_file)
        #all_summary holds the survey response data as a pandas dataframe
        all_summary = pd.read_excel(excel_file)
        #remove all rows (people cases) with duplicate emails except last entered row by that email person
        all_summary=all_summary.drop_duplicates(subset=['email_address'], keep='last').reset_index(drop=True)
        #remove all rows (people cases) with duplicate NAMES except last entered row by that name person
        all_summary=all_summary.drop_duplicates(subset=['fullname'], keep='last').reset_index(drop=True)
        #Get indices for non gmails
        non_gmails_indices = all_summary[all_summary['email_address'].str.endswith("@gmail.com") == False].index
        dropped_ppl=[all_summary["fullname"][i] for i in list(non_gmails_indices)]
        all_summary=all_summary.drop(non_gmails_indices).reset_index(drop=True)

        #deletes emails that are too long (greater than 300 chars) because they would slow down the program and no legit emails are longer than 300 chars
        too_long_indices = all_summary[all_summary['email_address'].str.len() > 300].index
        dropped_ppl=dropped_ppl + [all_summary["fullname"][i] for i in list(too_long_indices)]
        all_summary=all_summary.drop(too_long_indices).reset_index(drop=True)

        self.all_summary = all_summary

        #all_emails holds the final list of emails w no duplicate emails
        self.all_emails=list(all_summary["email_address"])
        #
        # #desired for the desired number of ppl per group
        # self.desired = int(input("How many people would you like in a group? "))
        #
        # #number of total calls
        # self.num_calls = int(input("How many times do you want people to call? "))
        #
        # #number of total threads
        # self.num_threads = int(input("How many threads/tabs/windows do you want to use? More means the program runs faster but takes more memory. "))

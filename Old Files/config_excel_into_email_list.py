#import pandas package for doing stuff with data
import pandas as pd
import os

#define an initial function that when run, initializes variables
def init():
    #make All_Summary a global variable we can use across files
    global All_Summary

    #get current directory path on specific computer using os    
    dir_path = os.path.dirname(os.path.realpath('Virtual Visitas (Responses).xlsx'))
    #file location for respones excel file
    excel_file = dir_path + '\\Virtual Visitas (Responses).xlsx'
    #All_Summary holds the survey response data as a pandas dataframe
    All_Summary = pd.read_excel(excel_file)
    #remove all rows (people cases) with duplicate emails except last entered row by that email person
    All_Summary=All_Summary.drop_duplicates(subset=['Email Address'], keep='last').reset_index(drop=True)
    #remove all rows (people cases) with duplicate NAMES except last entered row by that name person
    All_Summary=All_Summary.drop_duplicates(subset=['Full Name'], keep='last').reset_index(drop=True)
    #Get indices for non gmails
    non_gmails_indices = All_Summary[All_Summary['Email Address'].str.endswith("@gmail.com") == False].index
    #deletes emails that are too long (greater than 300 chars) because they would slow down the program and no legit emails are longer than 300 chars
    too_long_indices = All_Summary[len(All_Summary['Email Address'].str) > 300].index
    # Delete these row indexes from dataFrame
    All_Summary=All_Summary.drop(non_gmails_indices).reset_index(drop=True)
    All_Summary=All_Summary.drop(too_long_indices).reset_index(drop=True)
    
    #To optimize things, we should keep this stuff in a pd.dataframe instead of turning it into a list, because pd is more efficient.

    #global variable allEmailsNoDuplicates holds the final list of emails w no duplicate emails
    global allEmailsNoDuplicates
    allEmailsNoDuplicates=list(All_Summary["Email Address"])
    
    #create global variable desired for the desired number of ppl per group
    global desired
    desired = int(input("How many people would you like in a group? "))



#
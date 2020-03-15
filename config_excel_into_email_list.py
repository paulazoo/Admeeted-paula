#import pandas package for doing stuff with data
import pandas as pd

#define an initial function that when run, initializes variables
def init():
    #make All_Summary a global variable we can use across files
    global All_Summary
    #In future, use the function from library os to automatically get path in case of the error.
    excel_file = 'Testers Virtual Visitas (Responses).xlsx'
    #excel_file = pd.read_excel("Testers Virtual Visitas (Responses).xlsx")
    #All_Summary holds the survey response data as a pandas dataframe
    All_Summary = pd.read_excel(excel_file)
    #remove all rows (people cases) with duplicate emails except last entered row by that email person
    All_Summary=All_Summary.drop_duplicates(subset=['Email Address'], keep='last').reset_index(drop=True)
    #remove all rows (people cases) with duplicate NAMES except last entered row by that name person
    All_Summary=All_Summary.drop_duplicates(subset=['Full Name'], keep='last').reset_index(drop=True)
    
    #get the email column from the survey data and store in Email_Summary
    Email_Summary = All_Summary["Email Address"]
    #drop empty emails
    Email_Summary = Email_Summary.dropna()

    print(All_Summary["Email Address"])
    #Get indices for non gmails
    non_gmails_indices = All_Summary[All_Summary['Email Address'].str.endswith("@gmail.com") == False].index
    # Delete these row indexes from dataFrame
    All_Summary=All_Summary.drop(non_gmails_indices).reset_index(drop=True)
    print(All_Summary["Email Address"])
    print(All_Summary["Full Name"])
    
    #To optimize things, we should keep this stuff in a pd.dataframe instead of turning it into a list, because pd is more efficient.

    #global variable allEmailsNoDuplicates holds the final list of emails w no duplicate emails
    global allEmailsNoDuplicates
    allEmailsNoDuplicates=list(All_Summary["Email Address"])
    
    #create global variable desired for the desired number of ppl per group
    global desired
    desired = int(input("How many people would you like in a group? "))

init()
    


#import pandas package for doing stuff with data
import pandas as pd

#define an initial function that when run, initializes variables
def init():
    #make All_Summary a global variable we can use across files
    global All_Summary
    excel_file = r'C:\Users\alber\OneDrive - Georgia Institute of Technology\GitHub\VirtualVisitas\Programming Clubs Signup (Responses).xlsx'
    #All_Summary holds the survey response data as a pandas dataframe
    All_Summary = pd.read_excel(excel_file)
    #remove all rows (people) with duplicate emails except last entered row by that email person
    All_Summary=All_Summary.drop_duplicates(subset=['Email Address'], keep='last').reset_index(drop=True)
    
    #get the email column from the survey data and store in Email_Summary
    Email_Summary = All_Summary["Email Address"]
    #drop empty emails
    Email_Summary = Email_Summary.dropna()
    #start a list
    allEmails = []
    #create a list allEmails, adding on every email from
    for i in Email_Summary:
        if i.endswith("@gmail.com") and len(i) < 150:
          allEmails.append(i)
    #global variable allEmailsNoDuplicates holds the final list of emails w no duplicate emails
    global allEmailsNoDuplicates
    allEmailsNoDuplicates=list(allEmails)
    
    #create global variable desired for the desired number of ppl per group
    global desired
    desired = int(input("How many people would you like in a group? "))
    


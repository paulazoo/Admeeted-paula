#import pandas package for doing stuff with data
import pandas as pd
import os

#define an initial function that when run, initializes variables
def init(excel_name):
    #make All_Summary a global variable we can use across files
    global All_Summary

    #get current directory path on specific computer using os    
    dir_path = os.path.dirname(os.path.realpath(excel_name))
    print(dir_path)
    #file location for respones excel file
    excel_file = dir_path + "\\" + excel_name
    #All_Summary holds the survey response data as a pandas dataframe
    All_Summary = pd.read_excel(excel_file)
    #remove all rows (people cases) with duplicate emails except last entered row by that email person
    All_Summary=All_Summary.drop_duplicates(subset=['Email Address'], keep='last').reset_index(drop=True)
    #remove all rows (people cases) with duplicate NAMES except last entered row by that name person
    All_Summary=All_Summary.drop_duplicates(subset=['Full Name'], keep='last').reset_index(drop=True)
    
    global Dropped_ppl
    #Get indices for non gmails
    non_gmails_indices = All_Summary[All_Summary['Email Address'].str.endswith("@gmail.com") == False].index
    Dropped_ppl=[All_Summary["Full Name"][i] for i in list(non_gmails_indices)]
    All_Summary=All_Summary.drop(non_gmails_indices).reset_index(drop=True)
    
    #Get indices for non participating (CANT call at the time)
    non_participating_indices = All_Summary[All_Summary['Will you join the Wednesday 3:00 PM EST call? If you select yes, please participate; otherwise, it hurts the experience for others. :) '].str.endswith("Yes") == False].index
    #non_participating_indices2 = All_Summary[All_Summary['Will you join the Wednesday 3:00 PM EST call? If you select yes, please participate; otherwise, it hurts the experience for others. :) '].str.len() == 0].index
    Dropped_ppl=Dropped_ppl + [All_Summary["Full Name"][i] for i in list(non_participating_indices)]
    #Dropped_ppl=Dropped_ppl + [All_Summary["Full Name"][i] for i in list(non_participating_indices2)]
    All_Summary=All_Summary.drop(non_participating_indices).reset_index(drop=True)
    
    #deletes emails that are too long (greater than 300 chars) because they would slow down the program and no legit emails are longer than 300 chars
    too_long_indices = All_Summary[All_Summary['Email Address'].str.len() > 300].index  
    Dropped_ppl=Dropped_ppl + [All_Summary["Full Name"][i] for i in list(too_long_indices)]
    All_Summary=All_Summary.drop(too_long_indices).reset_index(drop=True)
    
    #print ppl whos emails didn't make it
    
    #write the full names of dropped gmails into a file
    with open("dropped_ppl.txt", "w") as outfile:
        outfile.write("\n".join(Dropped_ppl))

    #Delete these row indexes from dataFrame    
    
    
    
    #To optimize things, we should keep this stuff in a pd.dataframe instead of turning it into a list, because pd is more efficient.

    #global variable allEmailsNoDuplicates holds the final list of emails w no duplicate emails
    global allEmailsNoDuplicates
    allEmailsNoDuplicates=list(All_Summary["Email Address"])
    
    #create global variable desired for the desired number of ppl per group
    global desired
    desired = int(input("How many people would you like in a group? "))




#
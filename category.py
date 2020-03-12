import pandas as pd

def get_category_emails(All_Summary,allEmailsNoDuplicates,category):

#    category = input("Do groups by which category?")
    #get relevant category column
    category_Summary=All_Summary[category]
    
    #go through each category value
    category_strs=category_Summary.drop_duplicates()
    #list of category lists
    by_category=[]
    #relevant category value
    for category_val in category_strs:
        # print(major)
        #index of correct category values in category column
        category_yes=category_Summary[category_Summary==category_val].index
        category_yes=pd.Index.tolist(category_yes)
        # print(category_yes)
        
        #get specific emails that are correct e.g. 'History' in 'Major' column emails
        specific_emails = [allEmailsNoDuplicates[i] for i in category_yes]
        # print(specific_emails)
        by_category.append(specific_emails)
    print(by_category)
    return by_category



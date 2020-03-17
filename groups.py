import pandas as pd
import random
#returns a list of the subgroups (which are also lists themselves) of the emails.
def createGroups(allEmails, desired, callNum):
    #shuffle the list of emails
    random.shuffle(allEmails)
    #if the desired group size is more than the number of emails, just put everyone into one group
    if desired > len(allEmails):
        subgroups = [allEmails]
    #make subgroups the length of the desired number of ppl per group from the shuffled email list
    else:
        subgroups = [[callNum] + allEmails[x:x + desired] for x in range(0, len(allEmails), desired)]
        #if there's a group with less than desired number of people, evenly distribute amongst the other groups
        lastLen = len(subgroups[-1])
        if lastLen < desired:
            for x in range(lastLen):
                # if the remainder in the last group is larger than the number of subgroups, then it will add multiple people to the other groups
                subgroups[x % len(subgroups)].append(subgroups[-1][x])
                subgroups[-1][x] = 0

    subgroups = [x for x in subgroups if x != []]
    counter = 0
    #For efficiency, edit this to just check the last group in subgroups. Otherwise, could cause a bug
    for i in subgroups:
        for x in i:
            if x == 0:
                counter += 1
    if counter != 0:
        subgroups.pop(-1)
    return subgroups

#%%
#returns a list of groups from specified category, where each group is a list of emails for one specific category value (first value for each ans)
def get_category_emails(All_Summary,allEmails,category):
    #get the data for the relevant category
    category_Summary=All_Summary[category]
    #turn each multichoose answer into a list of chosen multichoose answers
    category_list = [(category_Summary[i].split(", ")) for i in range(0,len(category_Summary))]
    
    #get only the first ans for ans with multichoose
    category_firsts=[ans[0] for ans in category_list]
    print(category_firsts)
    
    #get all existing values in the category w no duplicates
    category_strs=list(set(category_firsts))
    
    #list of category lists
    by_category=[]
    #relevant category value
    for category_val in category_strs:
        #print(category_val)
        
        #indices of correct category values in category_firsts list
        category_yes=[i for i, x in enumerate(category_firsts) if x == category_val]
        #print(category_yes)
        
        #get specific emails that are correct e.g. 'History' in 'Major' column emails
        specific_emails = [allEmails[i] for i in category_yes]
        #print(specific_emails)
        
        #add that email list into by_category list
        by_category.append(specific_emails)
    print(by_category)
    return by_category, category_strs

#%%
def get_multicategory_emails(All_Summary,allEmails,category):
    #get the data for the relevant category
    category_Summary=All_Summary[category]
    #turn each multichoose answer into a list of chosen multichoose answers
    category_list = [(category_Summary[i].split(", ")) for i in range(0,len(category_Summary))]
    
    #get all existing values in the category w no duplicates
    all_category_vals=list(set([j for i in category_list for j in i]))
    
    #initialize email list for category
    by_category=[]
    #for each category value e.g. for each genre
    for category_val in all_category_vals:
        #initialize an email list for specific genre
        specific_emails=[]
        #for each answer in category list
        for idx, ans in enumerate(category_list):
            #if the specific genre is in the answer
            if category_val in ans:
                #add that email to the specific_emails list
                specific_emails.append(allEmails[idx])
        #check specific emails list
        print(category_val, ": ", specific_emails)
        #add this genre specific emails list to the general list of lists of emails by genre
        by_category.append(specific_emails)
    return by_category


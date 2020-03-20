import pandas as pd
import random
#returns a list of the subgroups (which are also lists themselves) of the emails.
def create_groups(all_emails, desired, call_num):
    #shuffle the list of emails
    random.shuffle(all_emails)
    #if the desired group size is more than the number of emails, just put everyone into one group
    if desired > len(all_emails):
        subgroups = [[call_num] + all_emails]
    #make subgroups the length of the desired number of ppl per group from the shuffled email list
    else:
        subgroups = [all_emails[(x) : (x + desired)] for x in range(0, len(all_emails), desired)]
        #first element of every group within subgroups is the call_num
        [subgroups[i].insert(0,call_num) for i in range(0,len(subgroups))]
        #print(subgroups)
    #if there's a group with less than desired number of people, evenly distribute amongst the other groups
        lastLen = len(subgroups[-1])
        if lastLen < desired+1:
            for x in range(1,lastLen):
                # if the remainder in the last group is larger than the number of subgroups, then it will add multiple people to the other groups
                subgroups[(x-1) % len(subgroups)].append(subgroups[-1][x])
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
    #print(subgroups)
    return subgroups

#%%
#returns a list of groups from specified category, where each group is a list of emails for one specific category value (first value for each ans)
def get_category_firsts(all_summary,all_emails,category):
    #get the data for the relevant category
    category_Summary=all_summary[category]
    #turn each multichoose answer into a list of chosen multichoose answers
    category_list = [(category_Summary[i].split(", ")) for i in range(0,len(category_Summary))]
    #get only the first ans for ans with multichoose...
    category_firsts=[ans[0] for ans in category_list]
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
        specific_emails = [all_emails[i] for i in category_yes]
        #print(specific_emails)
        #add that email list into by_category list
        by_category.append(specific_emails)
    #check final by_category lists of category_val lists
    print(by_category)
    #first return is by_category list of lists of emails, second is the category_val names, same index
    return by_category, category_strs

#%%
#returns a list of groups from specified category, where each group is a list of emails for one specific category value (first value for each ans)
def get_category_random(all_summary,all_emails,category):
    #get the data for the relevant category
    category_Summary=all_summary[category]
    
    #turn each multichoose answer into a list of chosen multichoose answers
    category_list = [(category_Summary[i].split(", ")) for i in range(0,len(category_Summary))]
    
    #get only the first ans for ans with multichoose...
    category_firsts=[random.choice(ans) for ans in category_list]
    
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
        specific_emails = [all_emails[i] for i in category_yes]
        #print(specific_emails)
        
        #add that email list into by_category list
        by_category.append(specific_emails)
        
    #check final by_category lists of category_val lists
    print(by_category)
    
    #first return is by_category list of lists of emails, second is the category_val names, same index
    return by_category, category_strs

#%%
def get_multicategory_all(all_summary,all_emails,category):
    #get the data for the relevant category
    category_Summary=all_summary[category]
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
                specific_emails.append(all_emails[idx])
        #check specific emails list
        print(category_val, ": ", specific_emails)
        #add this genre specific emails list to the general list of lists of emails by genre
        by_category.append(specific_emails)
    return by_category


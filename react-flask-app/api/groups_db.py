import pandas as pd
import random
import logging
import numpy as np

#returns a list of the subgroups (which are also lists themselves) of the emails.
def create_groups(all_emails, desired, call_num):
    #shuffle the list of emails
    all_emails=np.array(all_emails)
    np.random.shuffle(all_emails)
    #if the desired group size is more than the number of emails, just put everyone into one group
    if desired > all_emails.shape[0]:
        created_groups = [np.insert(all_emails, 0, str(call_num)).tolist()]
    else:
        #split evenly into all_emails/desired arrays and stack these arrays into a big 2d array
        split_groups = np.array_split(all_emails, np.floor(all_emails.shape[0] / desired))
        logging.warning(split_groups)
        #first element of every group within subgroups is the call_num
        call_num_groups=[np.concatenate((np.array([call_num]), subgroup),axis=0) for subgroup in split_groups]
        created_groups=[l.tolist() for l in call_num_groups]
    
    #log that
    logging.warning(created_groups)

    return created_groups

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
        #logging.warning(category_val)
        #indices of correct category values in category_firsts list
        category_yes=[i for i, x in enumerate(category_firsts) if x == category_val]
        #logging.warning(category_yes)
        #get specific emails that are correct e.g. 'History' in 'Major' column emails
        specific_emails = [all_emails[i] for i in category_yes]
        #logging.warning(specific_emails)
        #add that email list into by_category list
        by_category.append(specific_emails)
    #check final by_category lists of category_val lists
    logging.warning(by_category)
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
        #logging.warning(category_val)
        
        #indices of correct category values in category_firsts list
        category_yes=[i for i, x in enumerate(category_firsts) if x == category_val]
        #logging.warning(category_yes)
        
        #get specific emails that are correct e.g. 'History' in 'Major' column emails
        specific_emails = [all_emails[i] for i in category_yes]
        #logging.warning(specific_emails)
        
        #add that email list into by_category list
        by_category.append(specific_emails)
        
    #check final by_category lists of category_val lists
    logging.warning(by_category)
    
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
        logging.warning(category_val, ": ", specific_emails)
        #add this genre specific emails list to the general list of lists of emails by genre
        by_category.append(specific_emails)
    return by_category

#%%
def make_call_groups(all_emails, desired, call_num, category, category_groups):
    #if category doesn't equal random
#    if category != "r":
#        #get by category groups
#        by_category, category_strs=get_category_random(all_summary, all_emails, category)
#        
#        #for groups too tiny
#        tiny_groups = [group for group in by_category if len(group)<3]
#        tiny_groups_strs = [category_strs[by_category.index(group)] for group in by_category if len(group)<=2]
#        big_groups_strs = [category_val for category_val in category_strs if category_val not in tiny_groups_strs]
#        
#        print("")
#        print("tiny groups: "+str(tiny_groups_strs))
#        print("big groups: "+str(big_groups_strs))
#        
#        for tiny_group_idx, tiny_group in enumerate(tiny_groups):
#            tiny_group_name=tiny_groups_strs[tiny_group_idx]
#            add_to = input("Combine tiny group "+tiny_group_name+" to which group? ")
#            #s to skip
#            while (add_to not in category_strs) and (add_to != "s"):
#                add_to = input(add_to+" is not a group. Combine tiny group "+tiny_group_name+" to which group? ")
#            if add_to != "s":
#                by_category[category_strs.index(add_to)]=by_category[category_strs.index(add_to)]+tiny_group
#                by_category.pop(category_strs.index(tiny_group_name))
#                category_strs.pop(category_strs.index(tiny_group_name))
#
#        for i in range(0,len(category_strs)):
#            #create_groups out of each by_category category value group
#            #all groups with the same category have the same call  
#            category_groups = category_groups + create_groups(by_category[i], desired, call_num)  
#    else:
        #for just random groups, run this
    category_groups = category_groups + create_groups(all_emails, desired, call_num)
        
    return category_groups

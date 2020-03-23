#%%
#get the data for the relevant category
all_summary=myparser.all_summary
#%%
#turn each multichoose answer into a list of chosen multichoose answers
category_summary=all_summary[category].str.split(", ")
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
#%%
#get the data for the relevant category
all_summary=myparser.all_summary

#turn each multichoose answer into a list of chosen multichoose answers
#get only the first ans for ans with multichoose...
all_summary[category]=all_summary[category].str.split(", ")
category_summary=all_summary[category].apply(lambda x : random.choice(x))
#get all existing values in the category w no duplicates
category_strs=list(set(category_summary))


#list of category lists
by_category=[]
#relevant category value
for category_val in category_strs:
    #logging.warning(category_val)
    #indices of correct category values in category_firsts list
    specific_emails=all_summary["Email Address"][category_summary == category_val]
    logging.warning(specific_emails.values)
    logging.warning(" ")
    #logging.warning(specific_emails)
    #add that email list into by_category list
    by_category.append(specific_emails.values)

#check final by_category lists of category_val lists
#logging.warning(np.array(by_category))
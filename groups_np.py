#%%

#shuffle the list of emails
np.random.shuffle(all_emails)
#if the desired group size is more than the number of emails, just put everyone into one group
if desired > all_emails.shape[0]:
    subgroups = np.insert(all_emails, 0, str(call_num))    
else:
    #split evenly into all_emails/desired arrays and stack these arrays into a big 2d array
    subgroups = np.stack(np.array_split(all_emails, np.floor(all_emails.shape[0] / desired)))
    #first element of every group within subgroups is the call_num
    subgroups=np.concatenate((np.full((subgroups.shape[0], 1), call_num), subgroups),axis=1)

#log that
logging.warning(subgroups)



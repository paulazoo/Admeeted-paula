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
        created_groups = [np.insert(all_emails, 0, call_num).tolist()]
    else:
        #split evenly into all_emails/desired arrays and stack these arrays into a big 2d array
        split_groups = np.array_split(all_emails, np.floor(all_emails.shape[0] / desired))
        logging.warning(split_groups)
        #first element of every group within subgroups is the call_num
        call_num_groups=[np.concatenate((np.array([call_num]), subgroup),axis=0) for subgroup in split_groups]
        created_groups=[l.tolist() for l in call_num_groups]

    #log that
    logging.warning(created_groups)
    print(f'Created Groups: {created_groups}')

    return created_groups


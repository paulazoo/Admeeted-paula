#%%
def get_group_by_call_num(giant_dict, before_string, call_num):
    
    call_num_groups=[x for x in giant_dict if (before_string+str(call_num)) in x]
    
    return call_num_groups

#%%
#using get_group_by_call_num
get_group_by_call_num(giant_dict, 'Call: ', 1)

#%%
#test sending message to all Call: 1s
msg="testing msg bot pls ignore: Say hi to each other!"
web=hangout_tools.write_in_group_hangout(web,groupName,waitTime1,msg)
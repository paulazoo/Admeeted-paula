
#%%
def get_group_by_call_num(giant_dict, before_string, call_num):
    
    call_num_groups=[x for x in giant_dict if (before_string+str(call_num)) in x]
    
    return call_num_groups

#%%
#using get_group_by_call_num
call_num_groups=get_group_by_call_num(giant_dict, 'IGNORE TEST Call: ', 2)

#%%
wait_time=1
group_name=call_num_groups[0]

#%%
import helpers
web=helpers.login(wait_time)

#%%
for group_name in call_num_groups:
    #test sending message to all Call: 1s
    msg="testing msg bot pls ignore: Say hi to each other!"
    web=hangout_tools.open_group_hangout(web, group_name, wait_time)
    web=hangout_tools.write_in_group_hangout(web,group_name,wait_time,msg)
    
    #%%
for group_name in call_num_groups:
    web=hangout_tools.open_group_hangout(web,group_name ,wait_time)
    web,call_url=hangout_tools.get_call_url(web,group_name,wait_time)
    msg="Join the hangout video call and say hi: "+call_url
    web=hangout_tools.write_in_group_hangout(web,group_name,wait_time,msg)
    
        #%%
for group_name in call_num_groups:
    web=hangout_tools.open_group_hangout(web,group_name ,wait_time)
    web=hangout_tools.add_to_group_hangout(web, group_name, wait_time, 'pkzr3@k12albemarle.org')
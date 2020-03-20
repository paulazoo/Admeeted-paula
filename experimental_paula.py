def msg_all():
    return
#%%
import hangout_tools
groupName='test t: 2 c: 3 g: 1'

waitTime1=2

web=hangout_tools.open_group_hangout(web,groupName ,waitTime1)
web,call_url=hangout_tools.get_call_url(web,groupName,waitTime1)
msg="Join the hangout video call and say hi: "+call_url
web=hangout_tools.write_in_group_hangout(web,groupName,waitTime1,msg)


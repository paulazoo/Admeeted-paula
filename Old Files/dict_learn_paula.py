#%%

wait_time = 2

category='Testing'
#login using the login function in logging_in.py
web=login(wait_time)
logging.warning("Login worked")

#get out of iframe for making groups
web.driver.switch_to.default_content()
time.sleep(wait_time)


#start creating the hangout for each group in the generatedGroups for each designated call
for subgroup in given_groups:
    #group_name from dict
    group_name=subgroup
    web = create_hangout(web, given_groups[subgroup], group_name, wait_time)
    logging.warning(group_name)
    #web, total_groups=create_hangout(web, subgroup, group_name, total_groups,wait_time)
    #move on to the next group
    #finished!
    logging.warning(str(group_name) +" created!")

#%%
def test_dicts(batch, thread_num):
    print(batch)
    print(thread_num)

#%%
for group in d:
    print(group)
    print(d[])
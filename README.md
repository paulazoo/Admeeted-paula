# VirtualVisitas

### Google Form link: https://docs.google.com/forms/d/e/1FAIpQLScrrI4c-SRt6blejIZLADnBDt98UUg-2pMxrfMiChnDykhkGw/viewform

### Find invites:
- from gmail: https://github.com/alzh9000/VirtualVisitas/blob/master/where_are_invites_gmail.jpeg
- from hangouts.google.com: https://github.com/alzh9000/VirtualVisitas/blob/master/where_are_invites_gmail.jpeg

### prereq packages:
- webbot
- random
- pandas
- time
- datetime
- selenium

### functions
- config.py: 
	- config.init(): initialize and define global variables at the start
- logging_in.py:
	- logging_in.login(waitTime1): start browser and login to hangouts function
- groups.py:
	- createGroups(allEmails, desired): create random groups w desired number of ppl per group
	- get_category_emails(All_Summary,allEmails,category): make list of groups from specified category, where each group is a list of emails for one specific category value
	- get_multicategory_emails(All_Summary,allEmails,category): get category emails, but for multichoose categories. Each possible category value gets a group list.
- hangout_tools.py:
	- open_group_hangout(web, groupName, waitTime1): open a specific group hangout
	- exit_group_hangout(web, groupName, waitTime1): exit an already open group hangout
	- call_group_hangout(web, groupName, waitTime1): start a call for a group hangout (that has already been opened)
	- write_in_group_hangout(web, groupName, waitTime1, message): write in an already open group hangout
	- add_to_group_hangout(web, groupName, waitTime1, email): add an email to an already open and existing group hangout


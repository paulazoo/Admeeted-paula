#%%
#initialize variables
#the config file cleans the data and gets the starting variable values
from config import ExcelParser

myparser = ExcelParser("Princeton'ing for Quaran-teens (Responses) (1).xlsx")

myparser.all_summary
myparser.desired
myparser.all_emails
myparser.num_calls
myparser.num_threads

df=myparser.all_summary
#%%
import random
class User:
    def __init__(self, fullname, organization):
        #Initializes the object
        #Creates a random 10 digit unique id
        self.id = random.randint(1000000000,(2**32)-2)
        self.fullName = fullname
        self.email = df.loc[df['Full Name'] == fullname, 'Email Address']
        self.organization = organization
        self.joinedOn = joinedOn
        self.year = df.loc[df['Full Name'] == fullname, 'Grade / Class at College']
        self.hometown = hometown
        self.major = major
        self.minor = minor
        self.music = music
        self.sports = sports
        self.interests = interests
        self.feedback = feedback
    def json(self):
        #Returns a json dictionary of the important variables
        return {'id': self.id,
        'fullName': self.fullName,
        'email': self.email,
        'organization': self.organization,
        'joinedOn': self.joinedOn,
        'year': self.year,
        'hometown': self.hometown,
        'major': self.major,
        'minor': self.minor,
        'music': list(self.music),
        'sports': list(self.sports),
        'interests': list(self.interests),
        'feedback': self.feedback}
    def __str__(self):
        #Cleanly prints out the variables for testing and development pursposes
        return("\nID: %s\nFull Name: %s\nEmail: %s\nOrganization: %s\nJoined On Timestamp: %s\nYear: %s\nHometown: %s\nMajor: %s\nMinor: %s\nMusic: %s\nSports: %s\nInterests: %s\nFeedback: %s\n"
        % (self.id, self.fullName, self.email, self.organization, self.joinedOn, self.year, self.hometown, self.major, self.minor, self.music, self.sports, self.interests, self.feedback))
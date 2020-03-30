import random

class User:

    def __init__(self, fullName, email, organization, joinedOn, year=None, hometown=None, major=(), minor=(), music=(), sports=(), interests=(), feedback=None):
        #Initializes the object

        #Creates a random 10 digit unique id
        # self.id = random.randint(1000000000,9999999999)

        self.fullName = fullName
        self.email = email
        self.organization = organization
        self.joinedOn = joinedOn
        self.year = year
        self.hometown = hometown
        self.major = major
        self.minor = minor
        self.music = music
        self.sports = sports
        self.interests = interests
        self.feedback = feedback

    def json(self):
        #Returns a json dictionary of the important variables
        return {
        'fullName': self.fullName,
        'email': self.email,
        'organization': self.organization,
        'joinedOn': self.joinedOn,
        'year': self.year,
        'hometown': self.hometown,
        'major': list(self.major),
        'minor': list(self.minor),
        'music': list(self.music),
        'sports': list(self.sports),
        'interests': list(self.interests),
        'feedback': self.feedback}

    def __str__(self):
        #Cleanly prints out the variables for testing and development pursposes
        return("\nFull Name: %s\nEmail: %s\nOrganization: %s\nJoined On Timestamp: %s\nYear: %s\nHometown: %s\nMajor: %s\nMinor: %s\nMusic: %s\nSports: %s\nInterests: %s\nFeedback: %s\n"
        % (self.fullName, self.email, self.organization, self.joinedOn, self.year, self.hometown, self.major, self.minor, self.music, self.sports, self.interests, self.feedback))

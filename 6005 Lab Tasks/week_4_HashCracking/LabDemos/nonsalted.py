"""
Several approaches to 

Crack a hashed password based on a password list

NOTE: There is no Salt this time.
"""

import hashlib
import time


# --- SOME MAGIC FOR TIMING
def timethis(func):
    def func_wrapper(*args, **kwargs):
        t1 = time.time()
        out = func(*args, **kwargs)
        t2 = time.time()
        print ("Took {0} Seconds".format(t2-t1))
        return out
    return func_wrapper


"""
------------------------------------------------------
APPROACH 1:  Go through the whole list and print a match
------------------------------------------------------
"""
#@timethis
def simpleCrack(theHash, passwordList):

    for item in passwordList:
        guessHash = hashlib.md5(item.encode()).hexdigest()
        if guessHash == theHash:
            print("Password Match found {0}".format(item))
    
#@timethis
def returnCrack(theHash, passwordList):
    """
    We can cut off some time, by returning when we find the password,
    This aviods going through the rest of the list
    """
    for item in passwordList:
        guessHash = hashlib.md5(item.encode()).hexdigest()
        if guessHash == theHash:
            return item  #Return the match if it is found
            
"""
-----------------------------------------
What about multiple passwords
-----------------------------------------
"""

def guessMultiple(hashes, passwordList):
    """
    One approach is to use the same approach we did for single 
    Hashes, by calling our cracking function multiple times 
    """

    for item in hashes:
        out = returnCrack(item, passwordList)
        print("Password of {0} == {1}".format(item, out))

def guessMultipleDict(hashes, passwordList):
    """
    Or we could create a lookup table of all possible hashes and then use that
    """

    theDict = {}
    for item in passwordList:
        theHash = hashlib.md5(item.encode()).hexdigest()
        theDict[theHash] = item

    for item in hashes:
        print("Hash for {0} is {1}".format(item, theDict.get(item)))


if __name__ == "__main__":
    import time

    #Read our input file
    fd = open("10-million-password-list-top-10000.txt", "r")
    passwordList = [x.strip() for x in fd.readlines()]  #And Stash in an array

    fd.close()

    #------ Test our function here ---------

    # CASE 1:  GO THROUGH THE WHOLE LIST, AND PRINT MATCH
    t1 = time.time()
    print("--- SINGLE HASH: WHOLE LIST ---")
    simpleCrack("24eb05d18318ac2db8b2b959315d10f2", passwordList)
    t2 = time.time()
    print("\tTook {0} Seconds".format(t2-t1))

    # CASE 2: GO THROUGH THE WHLE LIST AND RETURN IF WE MATCH (Quicker)
    t1 = time.time()
    print("--- SINGLE HASH:  Return When Found ---")
    out = returnCrack("24eb05d18318ac2db8b2b959315d10f2", passwordList)
    print("Password found {0}".format(out))
    t2 = time.time()
    print("\tTook {0} Seconds".format(t2-t1))


    print ("----- Multiple Hashes -----")
    UNSALTED = ["24eb05d18318ac2db8b2b959315d10f2",
                "ab4f63f9ac65152575886860dde480a1", 
                "11a7f956c37bf0459e9c80b16cc72107",
                "0e2b0bb3a925c7001d953983f9de9823",
                "bd1e13bdaab82581d4dc299eb9a3da0f"]

    t1 = time.time()
    guessMultiple(UNSALTED, passwordList)
    t2 = time.time()
    print("\tTook {0} Seconds".format(t2-t1))

    #And using a Dict for multiple Hashes
    t1 = time.time()
    guessMultipleDict(UNSALTED, passwordList)
    t2 = time.time()
    print("\tTook {0} Seconds".format(t2-t1))

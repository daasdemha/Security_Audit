"""
Code for generating Strong Random passwords
"""

import hashlib
import bcrypt
import random
import string
import time


def randomString(length):
    """
    Generate a random Alpanumeric String
    """

    alphabet = string.ascii_letters + string.digits + string.punctuation

    tmparr = []
    for x in range(length):
        tmparr.append(random.choice(alphabet))

    return "".join(tmparr)


def generateRandom(length):
    """
    Use SHA 512 to generate a random password of a a given length

    @length:  Length of password
    """

    plaintext = randomString(length)
    
    #A am not going to bother salting it (as essnetially) with a truely random
    #password we end up with a "salt"
    
    theHash = hashlib.sha256(plaintext.encode()).hexdigest()
    return plaintext, theHash

def generateBcrypt(length):
    """
    Generate a random Brcypt password with input of length length
    """
    plaintext = randomString(length)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plaintext.encode(), salt)
    return plaintext, hashed


def crackRandom(plaintext, thehash):
    """
    Crack a random password
    """

    #TODO  YOU need to implement this

    return plaintext == thehash


def crackBcrypt(plaintext, thehash):
    """
    Crack A Bcrypt random password
    """

    #TODO You need to implement this

    return plaintext == thehash

if __name__ == "__main__":

    plaintext, thehash = generateRandom(5)
    print ("Password is {0} Hash {1}".format(plaintext, thehash))

    startTime = time.time()
    out = crackRandom(plaintext, thehash)
    endTime = time.time()
    if out:
        
        print ("It took {0} Seconds".format(endTime - startTime))
    else:
        print ("You Failed to crack the password in {0} seconds".format(endTime - startTime))




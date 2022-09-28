#Code we put together in the live lab session


import hashlib

def hashPw(plaintext):
    hash = hashlib.md5(plaintext.encode()).hexdigest()
    return hash

def saltPw(plaintext, salt):
    salted = "{0}{1}".format(plaintext, salt)
    print("Salted is {0}".format(salted))
    hash = hashlib.md5(salted.encode()).hexdigest()
    return hash

STOREDSALT="SALT$1615a0c818849f86ab7797fb1a0c7d3c"



if __name__ == "__main__":
    #print(hashPw("foobar"))
    #print(saltPw("foobar", "SALT"))

    #To Decrypt Stalted we have two stages.
    #1. Split out Salt and Hash
    salt, hashedPw = STOREDSALT.split("$")
    
    #To Crack we need to 
    # 1. Hash the dictionary word with the SALT (From above)
    # 2. Comprare to the hash from the stroed password.

    wordList = ["dave", "foobar", "bleh", "coffee"]
    for word in wordList:
        dictHash = saltPw(word, salt)  #Hash our dctioary word with the salt.
        print(dictHash == hashedPw) #And Compare

    print("="*80)
    #Lets repeat with one of our exmaple words
    storedsalt, hashedPw = "rkKxLR$c35bf00b953186ec3be4916dd45deabc".split("$")
    print(salt)

    wordList = ["dave", "foobar", "bleh", "coffee"]
    for word in wordList:
        dictHash = saltPw(word, storedsalt)  #Hash our dctioary word with the salt.
        print(dictHash == hashedPw) #And Compare

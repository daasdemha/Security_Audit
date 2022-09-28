import time
import hashlib
import random
import string

def simpleCrack(wordlist, target):
    """
    Code to crack an md5 hash using a dictionary

    @param wordlist:  List of dictionary Words
    @param target:    The Hash we want to crack
    """
    result = []
    match = None
#Loop through all items in the password List
    for item in wordlist:

      item = item.strip() #Remove New Lines
      item = item + "SALT"
      #print ("Chekking {0}".format(item))
      #Create a hash for the item
      theHash = hashlib.md5(item.encode()).hexdigest()
      #Compare to our target
      for i in range(len(target)):

	      if theHash == target[i]:
	           print ("Password Match found {0}".format(item))

	           match = item
	           result.append(match)
    
    return result


def simpleSalt(plaintext):
    return "{0}SALT".format(plaintext)


salted=simpleSalt("foobar")
print(salted)



def genSalt():
    """ 
    Generate a Salt

    @param plaintext:  plaintext password
    @return A tuple of (saltedPw, salt)
    """


    salt = []
    for x in range(6):
    	salt.append(random.choice(string.ascii_letters))
    	
    	
    	

    return "".join(salt)




def checksaltedpass(wordlist, target):
    result = []
    wordlist = open("10-million-password-list-top-10000.txt", "r")
    #sal1 = target.split()  
    for item in wordlist:
        for t in target:


            item = item.strip() #Remove New Lines
            saltedplaintext = "{0}{1}".format(item, t.split("$")[0])

            #print ("Chekking {0}".format(item))
            #Create a hash for the item
            theHash = hashlib.md5(saltedplaintext.encode()).hexdigest()
            storedPw = "{0}${1}".format(t.split("$")[0], theHash)
        #Compare to our target
        for i in range(len(target)):


            print("\n")
            print(i, storedPw, " ==  ", target[i])


            if storedPw == target[i]:
                   print ("Password Match found {0}".format(item))


                   
                   result.append(item)


    return result







if __name__ == "__main__":

    #Our word list
    wordlist = open("10-million-password-list-top-10000.txt", "r")
    #Our Target Hash
    target = []  #Unknown Hash
    target.append("283140d63e0937fb652ff7066bbf5c2f")
    target.append("ba7c94b0431f30103c7eb5cdae180be6")
    target.append("ff0e0cefdceb54618f47767d17b95a12")
    target.append("ef98a984f8ab1341039f9f3344d80298")
    target.append("25e2262b5d8c95f7ece0bc4f30f5213d")

    target.append("bd1e13bdaab82581d4dc299eb9a3da0f")
    






    startTime = time.time()
    out_put = simpleCrack(wordlist, target)
    endTime = time.time()
    print ("Total of {0} Seconds".format(endTime - startTime))

    for i in range (len(out_put)):




    	print("word is " + out_put[i])

    

    salt1 = genSalt()
    plaintext = "foobar"
    saltedplaintext = "{0}{1}".format(plaintext, salt1)
    print(saltedplaintext)
    passwordhash = hashlib.md5(saltedplaintext.encode()).hexdigest()
    storedPw = "{0}${1}".format(salt1, passwordhash)
    print(storedPw)

    
    new_list = ["rkKxLR$c35bf00b953186ec3be4916dd45deabc", "MyEtoS$b0a56a1df2353c7629509a12a17f5a2d","kshhHk$9664b09bedf4ed95f1b7b024087cec12",\
"FMVbrf$6751d1e9a8ee57b383836596869cd94a","wKBUOm$981132067d1a4ef9e943b8c300071a55","wKBUOm$b07e255b73044c38d522bf380d7bb673"]
    print(checksaltedpass(wordlist, new_list))
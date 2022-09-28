import hashlib
import time  #So we can see how long things take
import string
import random
#Our List of passwords in a file

UNSALTED = ["24eb05d18318ac2db8b2b959315d10f2",
            "ab4f63f9ac65152575886860dde480a1",
            "11a7f956c37bf0459e9c80b16cc72107",
            "0e2b0bb3a925c7001d953983f9de9823",
            "bd1e13bdaab82581d4dc299eb9a3da0f"]

# Passwowrd Hashes salted uing teh simple salt strategy
SIMPLE_SALT = ["283140d63e0937fb652ff7066bbf5c2f",
               "ba7c94b0431f30103c7eb5cdae180be6",
               "ff0e0cefdceb54618f47767d17b95a12",
               "ef98a984f8ab1341039f9f3344d80298",
               "25e2262b5d8c95f7ece0bc4f30f5213d"]

#MD5 Salted with Random Salts (in <salt>$<hash> format)
MD5_SALT = ["rkKxLR$c35bf00b953186ec3be4916dd45deabc",
            "MyEtoS$b0a56a1df2353c7629509a12a17f5a2d",
            "kshhHk$9664b09bedf4ed95f1b7b024087cec12",
            "FMVbrf$6751d1e9a8ee57b383836596869cd94a",
            "wKBUOm$981132067d1a4ef9e943b8c300071a55"]

SHA512_SALT = ["kuxYZE$c4d82bdbd75562f3d6c6622dbf38663dd381665365cc54fa1f8a341bc705f93e6a4f9ef135765ed1cbf4d2ab115395b2439af4b0140b80e89551b5b02c3d4788",
               "gMpNRt$d5b35a1fdba16224c0588de40513968aefc36e0932df8b64fceac5314ab64fcbe71a0a91d34dd652d20eb679a790ea0a631bd4a4eaa4b6f4ea1bccd26159c48d",
               "VLzSQA$a5eaac2093c3178550c0469be27e55e0d8931ce0c38db7a23106cedf5f9f4008753e8e055d705a48c5ccf8cbddce7622b8e72d22b58f4048faf0750ba77e13e7",
               "wVsUgH$5057743ba865faa4fedb0aa59a9792cba3c7b308ba842d75e4974786af0f2d386a2cb6d93748aac0b277648d4bf4a3dcadb207eefb73d145b2531d695b0feb84",
               "xTGhNw$2eaceffd81c2cd6819afc3c91bcc6c493a2edd965682eec6894356bf3d1841c58623c0830ba4fc8d96864eb9f998236feb73985668b5badc996c33e5e586361c"]
               
BCRYPT = [b'$2b$12$CQdfZxhjQH83jY.RZNfGPegUWSL05J5Amekp5pmjXkAgvtuBynZzy',
          b'$2b$12$4YiyGckKJXQGKMkGwOqM5.JKTjJIMlwwdfHYHtLhfc38lFU9iZicK',
          b'$2b$12$8vMax8thp0D7G2yns8gY7unUmdZiiJKJrjhW7pRtoo.X4YDObRVCK',
          b'$2b$12$JE6BgAfbDdLgWNnMuaqyeuvhmXECqsnZPMXqO3Rv.pxrzT8Zn4wqy',
          b'$2b$12$YINaek/4qU8/k2egmjZxn.MYU7lVehNi8p94iEDFvM7MaS3BUlZKK']

def simpleSalt(plaintext):
    """Append a simple hardcoded salt of SALT to the plaintext 
    before hashing
    """
    return "{0}SALT".format(plaintext)


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




def simpleCrack(wordlist, target):
    """Re implement the Simple Crack code as a function
    
    @param wordlist
    @param target
    """    
    
    # TODO

    pass
  
    

if __name__ == "__main__":

    #Our word list
    wordlist = open("10-million-password-list-top-10000.txt", "r")
    #Our Target Hash
    target = "dd8fcb2c31ee2c6ebbc63f8cf22e7c16"  #Unknown Hash
    

    startTime = time.time()
    #simpleCrack(wordlist, target)

    endTime = time.time()
    print ("Total of {0} Seconds".format(endTime - startTime))

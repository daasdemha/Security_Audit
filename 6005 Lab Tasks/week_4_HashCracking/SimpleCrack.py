import hashlib
import time  #So we can see how long things take
#Our List of passwords in a file
fd = open("./10-million-password-list-top-10000.txt", "r")

#Our Target Hash
target = "dd8fcb2c31ee2c6ebbc63f8cf22e7c16"  #Unknown Hash


startTime = time.time()

match = None
#Loop through all items in the password List
for item in fd:
    item = item.strip() #Remove New Lines
    print ("Chekking {0}".format(item))
    #Create a hash for the item
    theHash = hashlib.md5(item.encode()).hexdigest()
    #Compare to our target
    if theHash == target:
        print ("Password Match found {0}".format(item))
        match = item


endTime = time.time()
print ("Match is {0}".format(match))
print ("Total of {0} Seconds".format(endTime - startTime))
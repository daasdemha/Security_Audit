from Crypto.Cipher import AES

#Our Static Key
KEY = b"ThisIsAStaticKey"
IV  = b"ThisIsAnStaticIV"

def encryptMessage(message, IV=None):
    """Encrypt a message using a static key"""

    #Create a AES object We use CFB as we dont need to Pad the object input
    cipher = AES.new(KEY, AES.MODE_CFB, iv=IV)

    #Encode the Data
    enciphered = cipher.encrypt(message)
    
    #The IV is automagically Generated for us
    IV = cipher.iv

    #REturn them
    return enciphered, IV
    
       

def decryptMessage(message, IV):
    """
    Given a message and a IV
    Decrypt the data using a static key
    """

    cipher = AES.new(KEY, AES.MODE_CFB, iv=iv)

    #Deode the Data
    deciphered = cipher.decrypt(message)

    return deciphered
 


if __name__ == "__main__":


    
    message = b"Hello World"

    #Use a Static IV
    code, iv = encryptMessage(message, IV)
    print("Cipher Text is {0}".format(code))
    print("IV is {0}".format(iv))

    #Then Decipher

    decode = decryptMessage(code, iv)
    print("Decoded Message {0}".format(decode))
    

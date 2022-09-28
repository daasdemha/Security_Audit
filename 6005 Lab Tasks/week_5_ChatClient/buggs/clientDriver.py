"""
Driver Code for the Buggs Chat Client
This is the Code I expect you to modify
"""

import socket
import logging

class ChatClient:
                           
    def __init__(self, host, port=4242):
        """
        Initialise the server to connect to a given host and port
        """
        self.log = logging.getLogger("CLIENT")
        self.log.debug("Initialise Client")
        self.host = host
        self.port = port

        
    def sendMessage(self, message):
        """Helper Function to send a message
        This is what we need to modify to send a message
        """        
        self.sock.sendall(message.encode())



    """
    -------------------------------------------------
    
    YOU DO NOT NEED TO MODIFY ANYTHING BELOW HERE
    --------------------------------------------------
    """

       
    def run(self):
        #Main Loop
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            self.sock.connect((self.host, self.port))
            while True:
                data = input(">")
                if data == "-1":
                    break
                self.sendMessage(data)
            
        self.sock.close()
"""
Driver Code for the Buggs Chat Client
This is the Code I expect you to modify
"""
import logging


import socketserver

import logging

class RequestHandler(socketserver.BaseRequestHandler):
    """
    This is a class to handle requests. Made to the Chat Client
    This class holds extra functionalty that is called 
    when we receive a message.

    You can add your encryption logic here
    """

    def __init__(self, server_address, RequestHandler, bind_and_activate=True):
        self.log = logging.getLogger("SERVER")
        socketserver.BaseRequestHandler.__init__(self,
                                                 server_address,
                                                 RequestHandler,
                                                 bind_and_activate)


    def processData(self, data):
        """
        And process the data 

        Add our Logic Here
        """
        self.log.debug("Message {0}".format(data))
        






        
        
        

        """
        -------------------------------------------------
    
        YOU DO NOT NEED TO MODIFY ANYTHING BELOW HERE

        --------------------------------------------------
        """
    
    def handle(self):
        """
        The Handle Function is called each time a socket connection in made
        It remains until the connection is closed.

        As we are threaded,  It means that we can deal with multiple clients 
        (in theory, there is some "fun" handling different addresses)

        This function will simply run untill the socket is closed.
        """
        self.log.debug("Connection from {0}".format(self.client_address))
        while True:
            data = self.request.recv(1024)
            #And Do whatever we want to do with it
            self.processData(data)
            #And Do Whatver Processing we want 
            
            #Check if our data is Empty (EOF) If so the connetion
            #Is Closed and we end.
            if data == b'':
                print("EOF")
                break


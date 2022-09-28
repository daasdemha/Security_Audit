"""
This is the Core network functionality for the server.

  - Creates a Request Handler to deal with data
  - Creates a TCP Handler, that will push each request into a new thread
  - A Simple Funciton that will send data back across the network

I dont really expect you to modify this.
"""

import socket
import socketserver
import logging

class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    And this is the Server Itself.
    
    Having it Threaded means (in theory) we could hanbdle connections from
    multiple clients.  However, we need to modify the client, to deal with addressing.
    That is left as an Excersise for the reader.
    """



# And To Test
if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    #Start a Server
    server = ChatServer(("127.0.0.1", 4242), RequestHandler)
    #server = True
    with server:
        #Start the Server Thread
        serverThread = threading.Thread(target = server.serve_forever)
        serverThread.deamon = True #Kill with the main process
        serverThread.start() #And Get the Thread running

        #And Now the Client
        client = ChatClient("127.0.0.1")
        client.run()
        
        server.shutdown()
        


"""
Main Driver Program for the Chat Client
"""

import threading

import logging

logging.basicConfig(level=logging.DEBUG)  # CHANGE THIS FOR LOG LEVELS

logging.warning("YOU ARE NOT EXPECTED TO IMPORT THIS CODE")
logging.warning("Run as $python main.py")

# And the REst of our imports
import network
import serverDriver
import clientDriver

if __name__ == "__main__":
    log = logging.getLogger("MAIN")

    print("You need to specify an address to connect to")
    print("for example:")
    print("  - 127.0.0.1 (for your machine)")
    print("  - 10.0.2.15 (for someone elses machine)")

    ipAddr = input(">")

    log.debug("Creating Server")

    # Listen on EVERY port
    server = network.ChatServer(("0.0.0.0", 4242), serverDriver.RequestHandler)

    # And Register the server so we can send data back

    with server:
        # Start the Server Thread
        serverThread = threading.Thread(target=server.serve_forever)
        serverThread.deamon = True  # Kill with the main process
        serverThread.start()  # And Get the Thread running

        # And Now the Client
        client = clientDriver.ChatClient(ipAddr)
        client.run()

        server.shutdown()



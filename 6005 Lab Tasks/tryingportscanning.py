import socket

def checkPort(target, port):
    """
    Attempt to open a socket based connection to a host and port

    If the port is open on the target return True
    Otherwise return False
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    returnCode = sock.connect_ex((target, port))

    #A return code of 0 means we have a successful connection
    if returnCode == 0:
        return True
    elif returnCode == 111:
        #111 is connection refused (ie Closed)
        return False


if __name__ == "__main__":
    for i in range(0,1024):
        isOpen = checkPort("127.0.0.1", i)
        if isOpen == True:
            print ("Port ", i, " on Localhost open {0}".format(isOpen))
        else:
            pass

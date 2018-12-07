import socket

def _getaddr(server, port): #obscured from user, gets address as a tuple (server, port) ; returns -1 on error
    try:
        return (socket.gethostbyname(server), int(port))
    except:
        return -1


def _createsocket(): #obscured from user, gets socket ; returns -1 on error
    try:
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        return -1


def client(server, port, call): #creates a client using server and port ; calls "call" when connected
    sock = _createsocket()
    if sock == -1:
        return -1
    addr = _getaddr(server, port)
    if addr == -1:
        return -1
    sock.connect(addr)
    call(sock)
    return 0

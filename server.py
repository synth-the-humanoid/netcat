import socket
import signal

def _getaddr(server, port): #obscured from user, returns a tuple of socket-compatable server and port, and -1 on error
    try:
        return (socket.gethostbyname(server), int(port))
    except:
        return -1


def _createsocket(): #obscured from user, returns a socket, and -1 on error
    try:
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        return -1


def server(server, port, clients, call): #starts running a server at "server" on "port", with "clients" as the amount of clients storable in a backlog(most OSes cap at 5, 1 usually works for small applications, and using the function "call", which is given two arguments: the socket used in the connection, and the addr tuple of the connecting client. returns -1 on error
    addr = _getaddr(server, port)
    if addr == -1:
        return -1
    sock = _createsocket()
    if sock == -1:
        return -1
    try:
        sock.bind(addr)
        sock.listen(clients)
        while(True):
            conSock, cliAddr = sock.accept()
            call(conSock, cliAddr)
            signal.signal(signal.SIGINT, conSock.close)
        return 0
    except:
        return -1

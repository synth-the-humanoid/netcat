import sys 	 ## used for sys.argv[] and sys.exit()
import synthsock ## library i wrote to simplify socket connections(mainly to teach myself better socket programming)
################### can be found at https://github.com/synth-the-humanoid/synthsock

def terminal(sock): ## is supposed to open a netcat-esque terminal, STDIN refers to request, and STDOUT is the return from the server
    print("$ ",end="") ## fancy input dialog, very verbose
    request = input() ## takes input from STDIN
    if request.lower() == "exit": ## checks if the user wants to exit this program
        sys.exit(0)
    request += "\n\n"
    sock.send(request.encode()) ## sends the request specified by the user, in a binary format
    current = sock.recv(4096) ## gets 4096 bytes from the server
    while(len(current) != 0): ## while the reply is not empty
        print(current, end="") ## print the current loaded chunk of reply
        current = sock.recv(4096)
    print("\n\n")
    return 0


argc = len(sys.argv) - 1 ## just sets up an easy way for a conditional to check how many arguments are provided

if argc < 2: ## check for valid command line arguments
    print("Usage: python netcat.py <server> <port>")
    sys.exit(0)

server = sys.argv[1] ## fetch command line arguments
port = sys.argv[2]

try:
    port = int(port) ## make sure the port number is a valid integer
except:
    print("Usage: python netcat.py <server> <port>")
    sys.exit(0)

while(True):
    try:
        synthsock.client(server, port, terminal)
    except:
        print("Connection Error")
        sys.exit(0)

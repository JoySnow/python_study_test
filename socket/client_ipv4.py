# The most easy try of python socket.
# Example from:
#   https://docs.python.org/2/library/socket.html
#
# Echo client program
import socket, sys

#HOST = 'daring.cwi.nl'    # The remote host
HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print sys.argv[1] 
s.sendall(sys.argv[1])
# s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)

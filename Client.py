import socket
import sys
from time import *
# TCP/IP Connection for a new Client server client 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP,PORT = sys.argv[1],sys.argv[2] #getting input from termianl
filename = sys.argv[3] #getting file name from the terminal


print 'IP is ', IP
print 'PORT is ', PORT
print 'Filename is ', filename

# Connect to the socket
server_add = (IP,int(PORT))

print 'Connection to :', server_add
clientSocket.connect(server_add) # Connected to the server
print 'Server Connected!'

sent_at = time()
print 'File Request sent at :', sent_at 
#sending a filename to the client
clientSocket.send(filename) # Requesting the filename from the server

inputData = clientSocket.recv(1024) # Receving the data from the sever 
rec_at = time()
print 'Received at :', rec_at
print 'Time Taken :', rec_at - sent_at

print 'Data received by client is: '
print inputData







import socket
from thread import *
import sys
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Prepare a sever socket

Host = '127.0.0.1'
PORT = 8112
serverAddress = (Host,PORT) # Host Port tuple

serverSocket.bind(serverAddress) # Bind to the specific server address
serverSocket.listen(1)

print 'Serving on port', serverAddress[1], 'on localhost ', serverAddress[0]

def clientThread(conn): # Function for multiThreading. Handling diffrent clients. 

    try:
        message = conn.recv(4096).decode('utf-8') # Decoding the message received to utf-8 format
        string_list = message.split(' ')

        if message =='helloWorld.html': # The first part of the if statement caters to the client on terminal
            filename = message
            filename = str(filename)
            print('Client request filename', filename)
            f= open(filename,'rb')

        else:
            method = string_list[0]     # The else part of the if statement caters to the browser client 
            req_file = string_list[1]
            print('Client request ', req_file)
            filename = req_file.split('?')[0]
            filename = filename.lstrip('/')
            f = open(filename,'rb')

        outputdata = f.read() 
        f.close()

        header = 'HTTP/1.1 200 OK\n' # Sending file header with html format
        header += 'Content-Type: ' + 'text/html' + '\n\n'

    except Exception as e:

        header = 'HTTP/1.1 404 Not Found\n\n'
        outputdata = '<html><body><center><h3>Error 404: File not found on client %s </h3><p>Python HTTP Server</p></center></body></html>'.encode(
            'utf-8')

    final_response = header.encode('utf-8')
    final_response += outputdata
    conn.send(final_response)
    conn.close()


#Fill in end
while True:

#Establish the connection
    print 'Ready to serve...'
    conn,addr = serverSocket.accept()
    print 'Connected with ', addr[0], ':', str(addr[1])
    start_new_thread(clientThread, (conn,)) #MultiThrading function call for diffrent clients 







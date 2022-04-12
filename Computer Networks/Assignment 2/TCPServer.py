###################
# James Brooks    #
# CSC 450-001     #
# January 5, 2022 #
# TCP Server      # 
###################

from socket import *
import sys

# Initialize variables
buffer = 1024
host = "127.0.0.1" # uses localhost
port = 12000 # port used in example

# Create the server
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((host, port))
serverSock.listen(1)
print("The server is ready to receive...\n")
# Wait until client connects

while True:
    # Accept connection from client
    (connectionSock, address) = serverSock.accept()
    # Receive and decode request from client
    data = connectionSock.recv(buffer).decode()
    print("HTTP request:")
    print(data)
    print("Host: " + host)
    # Isolate the file's name from the request
    fileName = ((data.split()[1])[1:])
    print("\nObject to be fetched: " + fileName)
    # Try to open the file
    try:
        # Open the file
        file = open(fileName)
        # Read and store the file data
        output = file.read(-1)
        # Display the object's contents and response message
        print("Object content:")
        print(output)
        print("\nHTTP response message:")
        response = ("HTTP/1.1 200 OK\n\n" + output)
        print(response)
        # Send response and the requested file
        connectionSock.send(response.encode())
    # If there is an error, the file is not found
    except IOError:
        # Display error code
        print("\nHTTP response message:")
        response = "HTTP/1.1 404 Not Found"
        print(response)
        # Send error code back to server
        connectionSock.send(response.encode())
    # Close the connection
    connectionSock.close()
    break

    

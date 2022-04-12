###################
# James Brooks    #
# CSC 450-001     #
# January 5, 2022 #
# TCP Client      #
###################

from socket import *
import sys

# Initialize variables
buffer = 1024

# Take arguments from command line
args = sys.argv[1:]

IP = args[0] # IP is first
port = int(args[1]) # then port
fileName = args[2] # then the desired file

# Create the client
clientSock = socket(AF_INET, SOCK_STREAM)
# Connect to the server (use localhost for IP and 12000 for the port)
clientSock.connect((IP, port))
# Fill the request using the arguments provided
request = ("GET /" + fileName + " HTTP/1.1")
# Display request being sent and host
print("HTTP request to server: \n" + request)
print("Host: " + IP)
# Send the request
clientSock.send(request.encode())
# Wait for response
response = clientSock.recv(buffer)
# Display the response
print("\nHTTP response from server:")
print(response.decode())
# Close the client
clientSock.close()

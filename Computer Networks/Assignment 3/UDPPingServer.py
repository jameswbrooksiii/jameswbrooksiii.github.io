####################
# James Brooks     #
# CSC 450-001      #
# January 14, 2022 #
# TCP Ping Server  # 
####################

# Import libraries
from socket import *
import sys
import random

# Initialize buffer
buffer = 1024

# Establish host (uses localhost)
host = "127.0.0.1"
# Establish given port
port = 12000

# Initialize server socket
serverSock = socket(AF_INET, SOCK_DGRAM)
serverSock.bind((host, port))

while True:
    # Receive segment from client
    segment, address = serverSock.recvfrom(buffer)
    # Simulate packet loss based on random chance
    if random.randint(1,10) > 4:
        # Send segment back to client if segment is not lost
        serverSock.sendto(segment, address)
    
        

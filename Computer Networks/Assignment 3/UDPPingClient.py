####################
# James Brooks     #
# CSC 450-001      #
# January 14, 2022 #
# UDP Ping Client  #
####################

# Import libraries
from socket import *
import sys
import datetime

# Initialize buffer
buffer = 1024

# Take arguments from command line
args = sys.argv[1:]

# IP is first argument after program call
IP = args[0]
# Port is next
port = int(args[1])
# Set up address for socket
address = (IP, port)
# The number of pings is the last argument
pings = int(args[2])

# Initialize socket
clientSock = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout to 1
clientSock.settimeout(1);

# Initialize variables
sentSegments = 0
lostSegments = 0
minimumTime = sys.maxsize
maximumTime = 0.0
totalTime = 0.0
currentPing = 1

print("Pinging " + IP + ":")

for i in range(pings):
    try:
        # Start the timer
        startTime = datetime.datetime.now()
        # Format current time for the segment
        formattedTime = (datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"))
        # Create the segment
        segment = "Ping " + str(currentPing) + " " + formattedTime
        # Send segment to server
        clientSock.sendto(segment.encode(), address)
        # Receive segment back from server
        response = clientSock.recvfrom(buffer)
        # Record the time after receiving
        endTime = datetime.datetime.now()
        # Calculate the round trip time in milliseconds
        roundTripTime = datetime.timedelta(milliseconds = 0)
        roundTripTime = endTime - startTime
        roundTripTime = roundTripTime/datetime.timedelta(milliseconds = 1)
        roundTripTime = float(roundTripTime)
        totalTime += roundTripTime
        # Update minimum and maximum times
        if roundTripTime < minimumTime:
            minimumTime = roundTripTime
        if roundTripTime > maximumTime:
            maximumTime = roundTripTime
        # Increase succesful segments and the current segment by 1
        sentSegments += 1
        currentPing += 1
        # Print the reply message with the segment
        print("Reply from " + IP + ": " + response[0].decode() + " time=" + str(roundTripTime) + "ms TTL=1")

    # If packet loss occurs
    except:
        # Increase failed segments and print the failed message
        lostSegments += 1
        print("Request timed out.")

# Calculate percentages and average time
lostPercentage = lostSegments/pings*100
lostPercentage = "{:.1f}".format(lostPercentage)
averageTime = totalTime/sentSegments
averageTime = "{:.1f}".format(averageTime)
# Print the ping statistics
print("\nPing statistics for " + IP + ":")
print("\tSegments: Sent: " + str(pings) + ", Received: " + str(sentSegments) + ", Lost: " + str(lostSegments) + " (" + str(lostPercentage) + "% Loss)")
print("Approximate round trip times in ms:")
print("\tMinimum: " + str(minimumTime) + ", Maximum: " + str(maximumTime) + ", Average: " + str(averageTime))
# Close the client socket
clientSock.close()

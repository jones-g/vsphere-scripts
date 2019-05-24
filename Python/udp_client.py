from socket import *
import string
import time

# 'host' should be the IP address of the VC server
host = "192.168.1.1"

# 'port' can be changed if something other than 902 needs to be tested
port = 902

# 'numtimes' can be modified if more than 10 packets need to be sent
numtimes = 10

# 'data' is the size in bytes of the packets to be sent
datasize = 100
data = bytearray(datasize)

UDPSock = socket(AF_INET, SOCK_DGRAM)

for x in range(numtimes):
        UDPSock.sendto(data, (host, port))
        time.sleep(0.0001)

UDPSock.close()
print("\nSent %s UDP packets over port %s to %s", (numtimes, port, host))
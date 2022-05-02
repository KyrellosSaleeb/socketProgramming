import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

dataToBeSent = "Hello, server!"

SendingData = dataToBeSent.encode("UTF-8")

s.sendto(SendingData,('localhost',10000))

RecData, address = s.recvfrom(1024)

data = RecData.decode("UTF-8")

print("Data Reccived From {}: \n {}".format(address,data))

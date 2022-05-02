import socket
                  #IP            #UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = 'localhost'
portNum = 10000

s.bind((ip,portNum))
#data    #ip+portNum          #1KB
RecData, Address = s.recvfrom(1024) #buffer size
#decoding the received data
data = RecData.decode("UTF-8")

data_to_be_sent = "Hello, client!"
#encoding for sending data
SenData = data_to_be_sent.encode("UTF-8")
#send
s.sendto(SenData,Address)

print("Data Reccived From {}: \n {}".format(Address,data))

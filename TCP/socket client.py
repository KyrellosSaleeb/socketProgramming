import socket
serverName = 'localhost'
serverPort =12000
clinetSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = input('input message in lowercase: ')
clinetSocket.sendto(message.encode("UTF-8"),(serverName,serverPort))
data, clientAddress = clinetSocket.recvfrom(2048)
print(data.decode("UTF-8"))
clinetSocket.close()
message = input('press enter to exit')


#UDP client
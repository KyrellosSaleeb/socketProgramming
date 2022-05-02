import socket
serverPort =12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready to recive")
while 1:
    data, clientAddress = serverSocket.recvfrom(2048)
    message = data.decode("UTF-8")
    print(message)
    modifiedmessage = message.upper()
    serverSocket.sendto(modifiedmessage.encode("UTF-8"), clientAddress)
#UDP Server
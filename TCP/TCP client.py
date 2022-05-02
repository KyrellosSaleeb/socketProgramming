import socket

host = 'localhost'
port = 10000
size = 1024
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
data= s.recv(size)
if len(data):
    print('Received: ', data.decode('UTF-8'))
    data = 'message goes here'
while len(data):
    message = input('input lowercase sentence (type quit to end connection)')
    s.send(message.encode('UTF-8'))
    data = s.recv(size)
    print('Received: ', data,decode('UTF-8'))
    if message == 'quit':
        data = ''
s.close

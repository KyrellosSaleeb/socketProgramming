import socket

#test case
#www.google.com
website = input("enter url: ")

ip = socket.gethostbyname(website)
locIP = socket.gethostbyname("localhost")
print(ip)
print("local host ip is: ",locIP)


#####################################################
#test case
#127.0.0.1
address = input("enter IP: ")
host = socket.gethostbyaddr(address)
print(host)

####################################################
#test case
#http
service = input("enter the service/protocol name: ")
portNum = socket.getservbyname(service)
print(portNum)

####################################################
#test case
#21
PortNumber = input("enter Port Number: ")
serviceName = socket.getservbyport(int(PortNumber))
print(serviceName)


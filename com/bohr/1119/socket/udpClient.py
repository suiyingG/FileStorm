from socket import *

HOST = 'localhost'
PORT = 7528
ADDR = (HOST, PORT)
BUFSIZ = 2048

udpClient = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpClient.sendto(data.encode('utf-8'), ADDR)
    data, ADDR = udpClient.recvfrom(BUFSIZ)
    if not data:
        break
    print(data)

udpClient.close()
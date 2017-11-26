from socket import *
from time import ctime

HOST = ''
PORT = 7528
ADDR = (HOST, PORT)
BUFSIZ = 2048

udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(ADDR)

while True:
    print('Waiting for connection...')
    data, addr = udpServer.recvfrom(BUFSIZ)
    a = '[%s] %s' %(ctime(), data)
    udpServer.sendto(a.encode('utf-8'), addr)
    print('...recived from and returned to:',addr)

udpServer.close()
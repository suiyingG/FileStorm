from socket import *
from time import ctime

HOST = ''
PORT = 7528
BUFSIZ = 2048
ADDR = (HOST, PORT)

tcpServer = socket(AF_INET, SOCK_STREAM)
tcpServer.bind(ADDR)
tcpServer.listen(3)

while True:
    print('Wating for connection ...')
    tcpCliSock, addr = tcpServer.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data)
        a = '[%s] %s' %(ctime(), data)
        print(type(a))
        tcpCliSock.send(a.encode('utf-8'))
    tcpCliSock.close()

tcpServer.close()
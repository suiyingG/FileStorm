from socket import *

HOST = '127.0.0.1'
PORT = 7528
BUFSIZ = 2048
ADDR = (HOST, PORT)

tcpSoctClient = socket(AF_INET, SOCK_STREAM)
tcpSoctClient.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpSoctClient.send(data.encode('utf-8'))
    data = tcpSoctClient.recv(BUFSIZ)

    if not data:
        break
    print(data.decode('utf-8'))

tcpSoctClient.close()
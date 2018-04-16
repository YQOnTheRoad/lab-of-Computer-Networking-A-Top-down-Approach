import socket
serverIp="127.0.0.1"
serverPort=12000
serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((serverIp,serverPort))
serverSocket.listen(1)
print("Web server is ready for connection...")
while True:
    connectionSocket,addr=serverSocket.accept()
    print("Accept new connection from %s:%s..." %addr)
    req_mes=connectionSocket.recv(1024)
    req_file=bytes.decode(req_mes).split(' ')[1]
    filePath=req_file[1:]
    with open(filePath,'rb') as f:
        if not f:
            connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
        else:
            connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')
            for line in f.readlines():
                connectionSocket.send(line)
    connectionSocket.close()
    print("connection from %s:%s closed." %addr)
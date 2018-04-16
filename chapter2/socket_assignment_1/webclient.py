import socket
serverName="127.0.0.1"
serverPort=12000
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.send(b'GET /br.html HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n')
buffer=[]
while True:
    d=clientSocket.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
clientSocket.close()
header,html=bytes.decode(data).split('\r\n\r\n',1)
print(header)
with open('page.html','wb') as f:
    f.write(str.encode(html))



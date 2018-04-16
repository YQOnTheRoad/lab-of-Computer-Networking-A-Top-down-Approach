import socket
serverName="172.20.10.2"
serverPort=12000
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=raw_input("Input lowercase sentence:")
clientSocket.send(sentence)
modifiedSentence=clientSocket.recv(1024)
print("From server:"+modifiedSentence)
clientSocket.close()
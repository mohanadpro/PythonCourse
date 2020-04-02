import  socket

# create client socket
clientSocket=socket.socket()

# connect to the server socket
clientSocket.connect(('localhost',2600))

# data that the client will send to the server
data=input('Enter the data')
clientSocket.send(bytes(data,'utf-8'))

print(clientSocket.recv(1024).decode())
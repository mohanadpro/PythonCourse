import  socket


#create server socket
serverSocket=socket.socket()

# determine the IP and Port as an object to configure the server
serverSocket.bind(('localhost',2600))
print("server is ready")

# determine the number of client which can the server listen to them 3
serverSocket.listen(3)

while True:
    # accept the client connection
    client,addr=serverSocket.accept()

    # receive the data that the client send and decode it to be a string
    data=client.recv(1024).decode()

    print(client.getpeername(),addr,data)

    # send data to client
    client.send(bytes('Welcome in Mohanad server','utf-8'))

    # close the client
    client.close()
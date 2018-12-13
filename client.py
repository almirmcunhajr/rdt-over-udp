from socket import *

class Client:
    clientSocket = socket(AF_INET,SOCK_DGRAM)

    def bind(cli_addr, cli_port): # Bind client socket
        clientSocket.bind((cli_addr, cli_port))
    
    def send(data, server_addr, server_port): # Send data to server
        pass



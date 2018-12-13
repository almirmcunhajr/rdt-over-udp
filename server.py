from socket import socket, AF_INET, SOCK_DGRAM
from common import ip_checksum

class Server:
    send_socket = socket(AF_INET,SOCK_DGRAM)
    recv_socket = socket(AF_INET,SOCK_DGRAM)
    expected_seq = 0

    def bind(self, serv_addr, serv_port): # Bind the server receiver socket
        self.recv_socket.bind((serv_addr, serv_port))
    
    def receive(self, cli_addr, cli_port): # Receive data from the client 
        dest = (cli_addr, cli_port)
        message, address = recv_socket.recvfrom(4096)

        checksum = message[:2]
        seq = message[2]
        content = content[3:]

        if ip_checksum(content) == checksum:
            resp = 'ACK'+seq
            send_socket(ip_checksum(resp)+resp, dest)
            if seq == str(self.expected_seq):
                self.expected_seq = 1-self.expected_seq
                return content
            else:
                resp = 'ACK'+str(1-self.expected_seq)
                send_socket(ip_checksum(resp)+resp, dest)
                return -1

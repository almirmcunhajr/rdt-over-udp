from socket import socket, AF_INET, SOCK_DGRAM, timeout
from common import ip_checksum

class Client:
    send_socket = socket(AF_INET,SOCK_DGRAM)
    recv_socket = socket(AF_INET,SOCK_DGRAM)
    seq = 0

    def bind(self, cli_addr, cli_port): # Bind the client receiver socket
        self.recv_socket.bind((cli_addr, cli_port))
        self.recv_socket.settimeout(1)
    
    def send(self, data, server_addr, server_port): # Send data to server
        ack_received = False
        dest = (server_addr, server_port)
        while not ack_received:
            send_socket.sendto(ip_checksum(data)+str(self.seq)+data, dest)
            try:
                message, address = recv_socket.recvfrom(4096)
            except timeout:
                pass
            else:
                checksum = message[:2]
                seq = message[5]
                if ip_checksum(message[2:]) == checksum and seq == str(self.seq):
                    ack_received = True
        self.seq = 1-self.seq
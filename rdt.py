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
            self.send_socket.sendto((ip_checksum(data) + str(self.seq) + data).encode('utf-8'), dest)
            try:
                message, address = self.recv_socket.recvfrom(4096)
                message = message.decode('utf-8')
            except timeout:
                pass
            else:
                checksum = message[:2]
                seq = message[5]
                if ip_checksum(message[2:]) == checksum and seq == str(self.seq):
                    ack_received = True
        self.seq = 1-self.seq

class Server:
    send_socket = socket(AF_INET,SOCK_DGRAM)
    recv_socket = socket(AF_INET,SOCK_DGRAM)
    expected_seq = 0

    def bind(self, serv_addr, serv_port): # Bind the server receiver socket
        self.recv_socket.bind((serv_addr, serv_port))
    
    def receive(self, cli_addr, cli_port): # Receive data from the client 
        message, address = self.recv_socket.recvfrom(4096)
        message = message.decode("utf-8")
        dest = (cli_addr, cli_port)

        checksum = message[:2]
        seq = message[2]
        content = message[3:]

        if ip_checksum(content) == checksum:
            resp = 'ACK' + seq
            self.send_socket.sendto((ip_checksum(resp) + resp).encode('utf-8'), dest)
            if seq == str(self.expected_seq):
                self.expected_seq = 1-self.expected_seq
                return str(content)
            else:
                resp = 'ACK' + str(1-self.expected_seq)
                self.send_socket.sendto((ip_checksum(resp) + resp).encode('utf-8'), dest)
                return -1
        return -1
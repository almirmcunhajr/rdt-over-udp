from socket import socket, AF_INET, SOCK_DGRAM, timeout
from common import ip_checksum

class Client:
    send_socket = socket(AF_INET,SOCK_DGRAM)
    recv_socket = socket(AF_INET,SOCK_DGRAM)
    seq = 0

    def bind(self, cli_addr, cli_port): # Bind the client receiver socket
        self.recv_port = cli_port
        self.recv_socket.bind((cli_addr, cli_port))
        self.recv_socket.settimeout(1)
    
    def send(self, data, server_addr, server_port): # Send data to server
        dest = (server_addr, server_port)
        pack = (
            str(self.recv_port) +
            ip_checksum(data) +
            str(self.seq) +
            data
        ).encode('utf-8')

        ack_received = False
        while not ack_received:
            self.send_socket.sendto(pack, dest)
            try:
                message, address = self.recv_socket.recvfrom(4096)
            except timeout:
                pass
            else:
                checksum = message[:2].decode('utf-8')
                seq = message[5]-48
                if ip_checksum(message[2:]) == checksum and seq == self.seq:
                    ack_received = True
        self.seq = 1-self.seq

class Server:
    send_socket = socket(AF_INET,SOCK_DGRAM)
    recv_socket = socket(AF_INET,SOCK_DGRAM)
    expected_seq = 0

    def bind(self, serv_addr, serv_port): # Bind the server receiver socket
        self.recv_socket.bind((serv_addr, serv_port))
    
    def receive(self): # Receive data from the client 
        message, address = self.recv_socket.recvfrom(4096)

        cli_port = message[:5].decode('utf-8')
        checksum = message[5:7].decode('utf-8')
        seq = message[7]-48
        content = message[8:].decode('utf-8')

        dest = ('localhost', int(cli_port))

        resp = 'ACK' + str(seq)
        pack = (
            ip_checksum(resp) +
            resp
        ).encode('utf-8')

        inv_resp = 'ACK' + str(1-self.expected_seq)
        inv_pack = (
            ip_checksum(inv_resp) +
            inv_resp
        ).encode('utf-8')

        if ip_checksum(content) == checksum:
            self.send_socket.sendto(pack, dest)
            if seq == self.expected_seq:
                self.expected_seq = 1-self.expected_seq
                return content
            else:
                self.send_socket.sendto(inv_pack, dest)
                return -1
        return -1
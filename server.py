import rdt

if __name__ == "__main__":
    server = rdt.Socket()

    server.bind('localhost', 12015)

    while True:
        print('Waiting for incoming data')
        content = server.receive()
        if content[2] != -1:
            print('Received data: ' + content[2])
            ans = content[2]
            server.send(ans, content[0], content[1])
        else:
            pass
            print('Unexpected data received')
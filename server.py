import rdt

if __name__ == "__main__":
    server = rdt.Server()

    server.bind('localhost', 12015)

    while True:
        print('Waiting for incoming data')
        content = server.receive()
        if content != -1:
            print('Received data: ' + content)
        else:
            pass
            print('Unexpected data received')
import rdt

if __name__ == "__main__":
    server = rdt.Server()

    server.bind('localhost', 12015)

    while True:
        print('Waiting for incoming data')
        content = server.receive('localhost', 14740)
        if content != -1:
            print('Received data: ' + content)
        else:
            print('Unexpected data received')
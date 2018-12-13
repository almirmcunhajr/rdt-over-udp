import rdt

if __name__ == "__main__":
    server = rdt.Server()

    server.bind('localhost', 12015)

    while True:
        content = server.receive()
        if content != -1:
            print(content)
        else print ('Unexpected data received')
import rdt

if __name__ == "__main__":
    client = rdt.Socket()

    client.bind('localhost', 14740)

    while True:
        content = input('Enter the string to send to server: ')
        client.send(content, 'localhost', 12015)
        ans = client.receive()
        if ans[2] != -1:
            print('Received data: ' + ans[2])
        else:
            pass
            print('Unexpected data received')
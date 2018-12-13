import rdt

if __name__ == "__main__":
    client = rdt.Client()

    client.bind('localhost', 14740)

    while True:
        content = input('Enter the string to send to server: ')
        client.send(content, 'localhost', 12015)
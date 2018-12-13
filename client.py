import rdt

if __name__ == "__main__":
    client = rdt.Client()

    client.bind('localhost', 14740)
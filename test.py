def receive(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        broadcast(data)

def broadcast(data):
    for client in clients:
        client.send(data)

def receive_all():
    for client in clients:
        receive(client)
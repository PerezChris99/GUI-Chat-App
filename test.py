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

def broadcast_all():
    for client in clients:
        broadcast(client)

def receive_all_except(client):
    for client in clients:
        if client!= client:
            receive(client)

def broadcast_all_except(client):
    for client in clients:
        if client!= client:
            broadcast(client)

def close_all():
    for client in clients:
        client.close()

def close_all_except(client):
    for client in clients:
        if client!= client:
            client.close()

def close_client(client):
    client.close()

def close_client_except(client):
    if client!= client:
        client.close()

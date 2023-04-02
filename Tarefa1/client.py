import socket

def start_cliente():
    HOST = 'localhost'  # Endereco IP do Servidor
    PORT = 5000  # Porta que o Servidor está

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    message = "Pode me prestar um serviço?"
    client.sendall(message.encode())
    data = client.recv(1024)
    response = data.decode()
    print(response)

start_cliente()

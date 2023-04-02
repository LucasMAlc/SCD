import socket
import threading

def handle_client(conn, addr):
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Mensagem recebida: {message}")
            response = f"Serviço prestado pela thread {threading.current_thread().name}"
            conn.sendall(response.encode())

def start_servidor():
    HOST = ''  # Endereco IP do Servidor
    PORT = 5000  # Porta que o Servidor está

    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor iniciado. Aguardando conexões em {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        thread.start()
        print(f"Nova conexão: {addr}, thread: {thread.name}")

start_servidor()

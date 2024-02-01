import socket
import threading

def process_message(message, protocol):
    print(f"Mensagem recebida ({protocol}): {message}")
    with open(f"mensagens_recebidas_{protocol.lower()}.txt", "a") as file:
        file.write(message + "\n")

def handle_tcp_client(client_socket, addr):
    print(f"Conexao TCP estabelecida com {addr}")
    data = client_socket.recv(1024)
    data_str = data.decode()
    process_message(data_str, "TCP")
    client_socket.close()

def udp_server():
    HOST = 'localhost'
    PORT = 9090

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))

    print("Servidor UDP aguardando conexoes...")
    while True:
        data, client_addr = server_socket.recvfrom(1024)
        print(f"Conexao UDP estabelecida com {client_addr}")
        data_str = data.decode()
        process_message(data_str, "UDP")

def tcp_server():
    HOST = 'localhost'
    PORT = 9090

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print("Servidor TCP aguardando conexoes...")
    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_tcp_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    udp_thread = threading.Thread(target=udp_server)
    tcp_thread = threading.Thread(target=tcp_server)

    udp_thread.start()
    tcp_thread.start()

    udp_thread.join()
    tcp_thread.join()


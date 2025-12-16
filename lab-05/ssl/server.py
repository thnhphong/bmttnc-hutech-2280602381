import socket
import ssl
import threading

server_address = ('localhost', 12345)
clients = []

def handle_client(client_socket):
    clients.append(client_socket)
    print("Connected:", client_socket.getpeername())

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Received:", data.decode('utf-8'))

            for client in clients[:]:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)

    except:
        if client_socket in clients:
            clients.remove(client_socket)
    finally:
        print("Disconnected:", client_socket.getpeername())
        client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(server_address)
server_socket.listen(5)

print("Server is waiting to connect...")

# ✅ Create SSL context ONCE (đúng hơn, nhanh hơn)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(
    certfile="./certificates/server-cert.crt",
    keyfile="./certificates/server-key.key"
)

while True:
    client_socket, client_address = server_socket.accept()
    ssl_socket = context.wrap_socket(client_socket, server_side=True)
    threading.Thread(target=handle_client, args=(ssl_socket,), daemon=True).start()

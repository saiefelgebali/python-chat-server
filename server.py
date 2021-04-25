import socket
import threading
from requests import get

# Host address
HOST_NAME = socket.gethostname()
LOCAL_IP = socket.gethostbyname(HOST_NAME)
SERVER = ''
PORT = 9090
ADDR = (SERVER, PORT)

# Connection Settings
HEADER_SIZE = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'

# Create TCP Internet Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Method to Handle Clients Connecting
def HandleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    while connected:
        msg_length = conn.recv(HEADER_SIZE).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            
            print(f"[{addr}] [{msg_length}]{msg}")
            conn.send("[SERVER] Message Recieved.".encode(FORMAT))
    conn.close()        

# Method for Starting Server
def Start():
    server.listen()
    print(f"[LISTENING] Server is listening on port {PORT}")
    acceptingConnections = True
    
    while acceptingConnections:
        conn, addr = server.accept()
        thread = threading.Thread(target=HandleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] Server is starting...")
Start()
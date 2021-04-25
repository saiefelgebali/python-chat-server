import socket

# Host address
SERVER = '127.0.0.1'
PORT = 9090
ADDR = (SERVER, PORT)

# Connection Settings
HEADER_SIZE = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'

# Create TCP Client & Connect to Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def Send(msg):
    # Sends initial header with size of incoming message
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER_SIZE - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def Start():
    connected = True

    while connected:
        message = input("Enter message: ")
        Send(message)
        if message == DISCONNECT_MSG:
            connected = False

Start()
import socket
import threading

HEADER = 64
PORT = 5055
# SERVER = socket.gethostbyname(socket.gethostname())

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('208.67.222.222', 80)) # Connect to Open DNS Public IP
        SERVER_IP = s.getsockname()[0]
    except Exception:
        SERVER_IP = '127.0.0.1'
    finally:
        s.close()
    return SERVER_IP

SERVER = get_ip()
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
RECEIVED_MESSAGE = 'Message received.'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            print(f'Message Length: {msg_length}')
            msg_length = int(msg_length)
            msg =  conn.recv(HEADER).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{addr}] {msg}')

            # message = RECEIVED_MESSAGE.encode(FORMAT)
            # msg_length = len(message)
            # send_length = str(msg_length).encode(FORMAT)
            # send_length += b' ' * (HEADER - len(send_length))

            # conn.send(send_length)
            # conn.send(message)
            conn.send(RECEIVED_MESSAGE.encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() -1 }')

print("[STARTING] Server is starting...")
start()
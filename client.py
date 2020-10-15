import socket
import time

HEADER = 64
SERVER = '192.168.5.105'
PORT = 5055
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    time.sleep(.001)

    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    # print(f'Send Length: {send_length}')
    # print(f'Message: {message}')
    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))
    print('==================')

send('Hello Everyone!')
send('Hello World!')
send('Hello Everyone!')
send('Hello Again!')
send(DISCONNECT_MESSAGE)
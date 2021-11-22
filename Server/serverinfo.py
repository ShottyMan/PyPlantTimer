import socket

HEADER = 64
PORT = 5252
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'

DISCONNECT = '!DISCONNECT'

ADDR = (SERVER, PORT)
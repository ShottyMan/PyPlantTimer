import socket

HEADER = 64
PORT = 5252
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(ADDR)
except socket.error as e:
    print(f"""[\x1b[38;5;{124}mError\x1b[0m]: No Connection Detected, Socket Error: \x1b[38;5;{124}m {e}\x1b[0m""")

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    if msg in ["!EXIT", "!DISCONNECT"]:
        return 0
    return 1


send("Hello, World")

Continue = 1

while True:
    Continue = send(input(f"[{ADDR}]: "))
    if Continue == 0:
        break


send(DISCONNECT_MESSAGE)

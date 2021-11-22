import socket
import threading
import asyncio
import serverinfo
import clienthandling

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

START_THREAD = threading.active_count()

SOCKET.bind(serverinfo.ADDR)

def main():
    SOCKET.listen()
    print("[SERVER]: Server is starting...")

    while True:
        conn, addr = SOCKET.accept()
        CLOSED = clienthandling.thread_handle_client(conn, addr)
        if CLOSED:
            break
        CURRENT_THREAD = threading.activeCount() - START_THREAD
        print(f"[ACTIVE CONNECTIONS] {CURRENT_THREAD}")

    
    print("Program closing")
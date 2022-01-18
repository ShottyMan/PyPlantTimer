import asyncio
import socket
import threading
import time

import serverinfo


class Queue(object):
    def __init__(self):
        self.item = []

    def __repr__(self):
        return "{}".format(self.item)

    def __str__(self):
        return "{}".format(self.item)

    def enqueue(self, add):
        self.item.insert(0, add)
        return True

    def size(self):
        return len(self.item)

    def isempty(self):
        return self.size() == 0

    def dequeue(self):
        return None if self.size() == 0 else self.item.pop()


queue = Queue()  # init the class


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(serverinfo.HEADER).decode(serverinfo.FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(serverinfo.FORMAT)
            if msg in [serverinfo.DISCONNECT, "!STOP"]:
                connected = False
            print(f"[{addr}] {msg}")
    if msg == "!STOP":
        queue.enqueue(True)
    conn.close()


def thread_handle_client(conn, addr):
    print("[Thread]: New thread has been created..")
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    thread.join()
    return queue.dequeue()

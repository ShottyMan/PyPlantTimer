import socket
import threading
import asyncio
import serverinfo
import time

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
        if self.size() == 0:
            return True
        else: 
            return False
    def dequeue(self):
        if self.size() == 0:
            return None
        else:
            return self.item.pop()


queue = Queue()

def handle_client(conn, addr):

    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True

    while connected:

        msg_length = conn.recv(serverinfo.HEADER).decode(serverinfo.FORMAT)

        if msg_length:

            msg_length = int(msg_length)

            msg = conn.recv(msg_length).decode(serverinfo.FORMAT)

            if msg == serverinfo.DISCONNECT:

                connected = False

            print(f"[{addr}] {msg}")


    
    conn.close()
    queue.enqueue(True)





def thread_handle_client(conn, addr):
    
    print("[Thread]: New thread has been created..")
    thread = threading.Thread(target=handle_client,args=(conn, addr))
    thread.start()
    thread.join()
    return queue.dequeue()

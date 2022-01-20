import socket
import threading
import asyncio
import serverinfo
import clienthandling
import scheduler
import re
import time

# from debug import d

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
START_THREAD = threading.active_count()
SOCKET.bind(serverinfo.ADDR)
WEEKDAYS = (
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
)


def make_event(user_input, sch_obj: scheduler.Scheduler):
    user_input = user_input.split()
    try:
        day = WEEKDAYS.index(user_input[1])
    except:
        print("Invalid day.")
        return -1
    try:
        time_tuple = tuple(int(x) for x in user_input[1].split(":"))
    except:
        print("Invalid time.")
        return -2
    sch_obj.new_event(day, time_tuple[0], time_tuple[1])
    return 0

local_control_queue = clienthandling.Queue()

def local_control():
    s = scheduler.Scheduler()
    while True:
        user_input = input(">: ")
        if user_input == "quit":
            break
        if user_input == "mkevent": # FIXME: this... doesn't work
            print(make_event(user_input, s))
        elif user_input == "showevents":
            print(s.event_dict)  # TODO: make this prettier
    # TODO: make debug work again

def main():
    
    while True:
        thread = threading.Thread(target=local_control)
        thread.start()
        if local_control_queue:
            print("[NOTICE]: Quitting Program...")
            break

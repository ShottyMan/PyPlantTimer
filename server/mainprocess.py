import socket
import threading
import asyncio
import serverinfo
import clienthandling
import scheduler
import re
import time
import os
from debug import d


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


# Create a queue for the Local control thread for allowing talking within and outside the thread.
local_control_queue = clienthandling.Queue()


def start_terminal():
    columns, lines = os.get_terminal_size()
    print(f"""\x1b[2J\x1b[{lines};0H""")


# This is the function we pass to the thread function to start a new thread.
def local_control():
    s = scheduler.Scheduler()
    start_terminal()
    d.dlog_debug("Thread has been started.")
    while True:
        user_input = input(">: ")
        if user_input == "quit":
            break
        if user_input == "mkevent":  # FIXME: this... doesn't work
            d.dlog_notice(make_event(user_input, s))
        elif user_input == "showevents":
            d.dlog_notice(s.event_dict)  # TODO: make this prettier
    # TODO: make debug work again
    local_control_queue.enqueue(True)


def main():
    # Started thread to allow input while outputting
    thread = threading.Thread(target=local_control)
    thread.start()

    time.sleep(2)

    seconds = 2
    while True:
        # Reminder if you want to pass arguements you can do args=*Place arguements here*
        time.sleep(2)
        d.dlog_debug("Testing" + str(os.get_terminal_size()) + f" seconds: {seconds}")
        if local_control_queue.dequeue():
            d.dlog_notice("Program closing...")
            break
        seconds += 2
    thread.join()

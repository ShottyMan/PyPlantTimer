import socket
import threading
import asyncio
import serverinfo
import clienthandling
import scheduler
import re
from debug import d

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

START_THREAD = threading.active_count()

SOCKET.bind(serverinfo.ADDR)


#Weekdays
WkDays = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY")

#Patterns
mkeventcmd = re.compile(r'mkevent')
mkeventflgs = re.compile(r'(?:[mM]on|[tT]ues|[wW]ednes|[tT]hurs|[fF]ri|[sS]at|[sS]un)day')
mkeventtime = re.compile(r'(?:0[\d]|1[\d]|2[0-4])-[0-5]\d')


def main():
    #SOCKET.listen()
    #print("[SERVER]: Server is starting...")

    #while True:
    #    conn, addr = SOCKET.accept()        
    #
    #    CURRENT_THREAD = threading.activeCount() - START_THREAD
    #
    #    print(f"[ACTIVE CONNECTIONS] {CURRENT_THREAD}")
    #
    #    clienthandling.thread_handle_client(conn, addr)"
            
    while True:
        inputcnsl = input(">: ")
        if inputcnsl == "quit":
            break
        else:
            if mkeventcmd.match(inputcnsl):

                day = mkeventflgs.findall(inputcnsl)
                
                time = mkeventtime.findall(inputcnsl)
                if (bool(day) != True) and (bool(time) != True):
                    
                    print("Invalid inputs, day and time are incorrectly inputed. Format is -Weekday H-M.")
                    
                elif bool(day) != True:
                    
                    print("Invalid Weekday pick a valid weekday.")
                    
                elif bool(time) != True:
                    
                    print("Time is incorrectly inputed time format is H-M")
                    
                else:
                    
                    d.Dlog("Differentiation Successful")
                    d.Dlog(str(day))

                    WeekdayFinal = []

                    DayIndex = 0

                    

                    for items in day:

                        WkDaysIndex = 0

                        for days in WkDays:
                            

                            if days == items.upper():

                                WeekdayFinal.append(DayIndex)

                                break

                            WkDaysIndex += 1

                        DayIndex += 1

                    print(WeekdayFinal[0])

                        

                print(day)
                print(time)

                

    
    print("Program closing")
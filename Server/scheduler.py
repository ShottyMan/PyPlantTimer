import datetime
import time
import pickle
import os


#print("Starting..")
def CheckingDirAndMaking():
    currentdir = os.getcwd()

    if os.path.exists(currentdir + "/.pkl"):
        print("Directory Already Exists.")
    else:
        NewPkl = os.path.join(currentdir, ".pkl")
        try:

            os.mkdir(NewPkl)

        except OSError as error:

            print(error)


def CheckingTimeEvent(ScheduleTime):
    CurrentTime = datetime.datetime.now()

    Weekday = CurrentTime.strftime('%A')

    Time = CurrentTime.strftime("%H:%M")

    if Weekday == ScheduleTime.strftime('%A') and Time == ScheduleTime.strftime("%H:%M"):
        
        print("[NOTICE] Event occured.")

    return True


def CreatingWeekdayEvent(Day, Hour, Minute):
    EventTime = Day + "-" + Hour + "-" + Minute
    
    EventTimeObj = datetime.strptime(EventTime, "%A-%H-%M")

    return EventTimeObj
    




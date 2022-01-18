import os
import pickle
import time
from datetime import datetime


# print("Starting..")
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
    CurrentTime = datetime.now()
    Weekday = CurrentTime.strftime("%A")
    Time = CurrentTime.strftime("%H:%M")
    temp = ScheduleTime.strftime("%A")
    temp2 = ScheduleTime.strftime("%H:%M")
    print("[Notice] Detecting Events")
    if Weekday != ScheduleTime.strftime("%A") or Time != ScheduleTime.strftime("%H:%M"):
        return False
    print("[NOTICE] Event occured.")
    return True


def CreatingWeekdayEvent(Day, HourMinute):
    currentdir = os.getcwd()
    EventTime = str(Day).title() + "-" + HourMinute
    EventTimeObj = datetime.strptime(EventTime, "%A-%H-%M")
    FileTerm = 0
    while True:
        try:
            print(currentdir + "/.pkl/" + "Event" + str(FileTerm) + ".pkl")
            if (
                os.path.exists(currentdir + "/.pkl/" + "Event" + str(FileTerm) + ".pkl")
                == False
            ):
                print("File does not exist.")
                pickle.dump(
                    EventTimeObj,
                    open(
                        currentdir + "/.pkl/" + "Event" + str(FileTerm) + ".pkl", "wb"
                    ),
                )
                break
            FileTerm += 1
        except OSError as error:
            print(error)
            break


def LoadEvent():
    currentdir = os.getcwd() + "/.pkl/"
    files = 0
    filedir = "Event" + str(files) + ".pkl"
    FileCount = 0
    while True:
        try:
            print(currentdir + "Event" + str(FileCount) + ".pkl")
            if os.path.exists(currentdir + "Event" + str(FileCount) + ".pkl") == True:
                FileCount += 1
            else:
                break
        except OSError as error:
            print(error)
            break
    file = []
    while True:
        if os.path.exists(currentdir + filedir):
            fileopen = open(currentdir + filedir, "rb")
            file.append(pickle.load(fileopen))
        elif os.path.exists(currentdir + filedir) == False:
            break
        files = 1 + files
        filedir = "Event" + str(files - 1) + ".pkl"
    return file


def ShowEvents():
    currentdir = os.getcwd()
    currentdir = currentdir + "/.pkl/"
    Files = os.scandir(currentdir)
    for items in Files:
        if items.is_file:
            print(items.name)

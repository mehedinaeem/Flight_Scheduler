import datetime as dt
import time
import winsound as ws

def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H:%M:%S")
        print("Current Time:", currentTime)
        if currentTime == setAlarmTimer:
            ws.PlaySound(r'path', ws.SND_ALIAS)
            break

def getAlarmTime(hour, minute, second):
    alarmSetTime = f"{hour:02d}:{minute:02d}:{second:02d}"
    alarm(alarmSetTime)

def set_alarm():
    try:
        hour = int(input("Enter the hour (0-23): "))
        minute = int(input("Enter the minute (0-59): "))
        second = int(input("Enter the second (0-59): "))

        if 0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60:
            getAlarmTime(hour, minute, second)
        else:
            print("Invalid input. Please enter valid time values.")

    except ValueError:
        print("Invalid input. Please enter valid integer values.")

if __name__ == "__main__":
    print("Remember to set time in 24-hour format!")
    set_alarm()

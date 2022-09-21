from plyer import notification
import time

def reminder():
    notification.notify(title = "break reminder", message="break time",timeout = 1)
while True:
    reminder()
    time.sleep(1200)
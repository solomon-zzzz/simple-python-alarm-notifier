import pygame
import win10toast
from win10toast import ToastNotifier
import time
import datetime

pygame.mixer.init()
toaster = ToastNotifier()
datetimeString = input("Enter date and time in this format dd/mm/yyyy hh:mm:ss: ").strip()
today = datetime.datetime.today()
try:
    target = datetime.datetime.strptime(datetimeString, "%d/%m/%Y %H:%M:%S")
    if target <= today:
        print("The specified time is in the past. Please set a future time.")
    else:
        totalTime = target - today
        seconds = totalTime.total_seconds()
        print("\nALARM CLOCK SET SUCCESSFULLY\n")
        time.sleep(seconds)
        toaster.show_toast("Alarm clock", "Wake Up", duration=10, threaded=True)
        pygame.mixer.music.load(r"C:\sinai\ringtone.mp3")
        pygame.mixer.music.play(-1)
        input("Press Enter to stop the alarm...")
        pygame.mixer.music.stop()
except ValueError as e:
    print(f"Error: {e}. Please enter the date and time in the correct format.")

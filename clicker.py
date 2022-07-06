import pyautogui as root
import time
from time import sleep

print("Welcome to the InstantClick!")

while True:
    clcks_amount = input("Enter the amount of clicks: ")
    clcks_amount = int(clcks_amount)
    interval_var = input("Enter the interval between clicks (in secs): ")
    interval_var = int(interval_var)
    timetospend = input("Enter the wait time before the click: ")
    timetospend = int(timetospend)

    time.sleep(timetospend)

    root.click(clicks=clcks_amount, interval=interval_var

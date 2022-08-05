import pyautogui as root
import time
from time import sleep

print("Welcome to the InstantClicker by Markella's! \n https://github.com/Markellas/InstantClicker")

while True:
    print("")
    clcks_amount = input("Enter the amount of clicks: ")
    clcks_amount = int(clcks_amount)
    print("")
    interval_var = input("Enter the interval between clicks (in secs): ")
    interval_var = int(interval_var)
    print("")
    timetospend = input("Enter the wait time before the click: ")
    timetospend = int(timetospend)
    print("")

    print(f"InstantClicker is waiting for {timetospend} seconds to you to place the cursor...")
    print("")

    time.sleep(timetospend)

    root.click(clicks=clcks_amount, interval=interval_var)

    print("Clicks were succsessful! Continue using InstantClicker if want"))

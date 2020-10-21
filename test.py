import pyautogui
import time
import random

time.sleep(3)

# take random number from 1-3
for x in range (0,101):
    number = random.randint(1,3)
    pyautogui.typewrite(str(number),interval=0)
    # print(number)
    pyautogui.press('enter')



import pyautogui
import time
time.sleep(5)

rec = "blabla"

for x in range (1,5):
    pyautogui.typewrite(rec, interval = 0.1)
    pyautogui.press('enter')

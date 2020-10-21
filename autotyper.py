# auto typer for verifikator

# keyboard and mouse libraries

import pyautogui
import time
import random
import keyboard



#reading source code file
place = "C:\\Users\\Rysco\\Desktop\\Auto typer\\ttt.cpp"
try:
   with open(place) as file:
      tekst = file.read()
except FileNotFoundError:
   tekst = None
print(tekst)




pyautogui.keyDown('ctrl')
pyautogui.keyDown('alt')


#print (pyautogui.position())

#pyautogui.moveTo(1000, 1000, duration=0.25)
n = random.randint(1,5)
#m = random.random()
print("Random float is: ", random.uniform(0,0.5))
print("waiting ", n, "seconds")
#print("m= ", m)
time.sleep(5)
#print("<")

pyautogui.typewrite(tekst, interval=0.1)
#pyautogui.typewrite("#include <iostream>\nusing namespace std;\n\nint main(){\n}", interval=0.1)
#pyautogui.write("#include iostream\n", interval=0.1)
#pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=0.1)
#pyautogui.write("<>={}|~()!;:", interval=0.1)

#rk = keyboard.record(until = 'Esc')
#time.sleep(2)
#keyboard.play(rk, speed_factor = 0.5)

pyautogui.keyUp('ctrl')
pyautogui.keyUp('alt')

from pyautogui import *

sleep(5)
print(position())

moveTo(1251, 10, 5)
click(1251, 10)
sleep(2)
moveTo(1342, 14, 5)
click(1342, 14)
sleep(2)
moveTo(1168, 32, 5)
sleep(2)

keyDown('alt')
sleep(0.2)
press('tab')
sleep(0.4)
keyUp('alt')

print("Your Minimization program is complete!")
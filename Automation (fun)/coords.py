import pyautogui
import time

def reset():
    pyautogui.moveTo(1, 1, duration= 1)


def scrsize():
    return pyautogui.size()


def page_login():
    pyautogui.sleep(20)
    pyautogui.click(500, 390)
    number = ['8','9','9','9','9','5','1','8','4','3']

    for x in range(10):
        pyautogui.sleep(0.2)
        pyautogui.press(number[x])
    pyautogui.sleep(0.2)
    pyautogui.press('Enter')

    pyautogui.sleep(5)
    pyautogui.click(850, 490)


def rc_status():
    pass


def altTab():
    pyautogui.keyDown('alt')
    pyautogui.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.sleep(0.5)
    pyautogui.keyUp('alt')


def copy():
    pyautogui.keyDown('ctrl')
    pyautogui.sleep(0.2)
    pyautogui.press('c')
    pyautogui.sleep(0.5)
    pyautogui.keyUp('ctrl')


def paste():
    pyautogui.keyDown('ctrl')
    pyautogui.sleep(0.2)
    pyautogui.press('v')
    pyautogui.sleep(0.5)
    pyautogui.keyUp('ctrl')


def press_tabs(num):
    for i in range(num - 1):
        pyautogui.press('tab')
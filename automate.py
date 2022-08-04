import pyautogui
import time

pyautogui.FAILSAFE = False

while True:

    time.sleep(60)
    for i in range(100):
        pyautogui.moveTo(0, i*5)
    for i in range(0, 3):
        with pyautogui.hold('win'):
            pyautogui.press('tab')  # presses = 2
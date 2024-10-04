import pyautogui
import random

pyautogui.FAILSAFE = False

while True:
    pyautogui.moveTo(random.randint(1, 1800), random.randint(1, 1800))
    pyautogui.click()
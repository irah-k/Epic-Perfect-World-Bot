import operator
import sys
import time
import ctypes
import pytesseract
import win32gui

import pyautogui
from pyautogui import press
from PIL import ImageGrab
from PIL import Image
from pynput import keyboard

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
pyautogui.FAILSAFE = False

w = win32gui

enemies = ['Nightscream Crystal']


## CHECK BEFORE STARTING:
# Banker position on screen

def find_target():
    img = ImageGrab.grab((550, 50, 750, 68))
    img = img.convert('L')
    img.save("temp.png")
    name = pytesseract.image_to_string(Image.open('temp.png'), config='--psm 7')
    try:
        lvl_idx = name.index("]") + 1
        return name[lvl_idx:].strip()
    except ValueError:
        print("ERROR: TARGET NOT CORRECTLY DETECTED")
        return ""
    except Exception:
        return ""


def valid_target():
    try:
        name = find_target()
    except NameError:
        return False
    if name in enemies:
        return True
    else:
        return False


def depositToBank():
    press('b')
    time.sleep(.2)
    # pyautogui.rightClick(1619, 1059)  # town teleport
    press('3')
    time.sleep(15)
    pyautogui.click(1750, 248)  # open coordinate
    time.sleep(.2)
    pyautogui.doubleClick(509, 106)  # click banker on coordinate
    time.sleep(8)
    press('esc')
    time.sleep(.2)
    pyautogui.doubleClick(955, 978)  # click banker npc
    time.sleep(1.5)
    pyautogui.doubleClick(120, 466)  # click safe service
    time.sleep(1)
    pyautogui.rightClick(1616, 1118)  # deposit bronze coins
    time.sleep(1)
    press('esc')
    time.sleep(.2)


def flyToCrystals():
    for i in range(10):
        press('space')
        time.sleep(.2)
    press('9')
    time.sleep(1)
    pyautogui.click(1750, 248)  # open coordinate
    time.sleep(.2)
    pyautogui.doubleClick(474, 126)  # click crystals on coordinate
    time.sleep(.5)
    pyautogui.keyDown('space')
    time.sleep(10)
    pyautogui.keyUp('space')
    time.sleep(25)
    press('esc')
    time.sleep(.5)
    press('9')
    time.sleep(.2)


def check_pause():
    global pause
    global pauseCounter
    if pyautogui.position() == (0, 0):
        pauseCounter += 1
    else:
        pause = False
        pauseCounter = 0

    if pauseCounter > 0:
        pause = True


count = 0
invalidCount = 0
pause = False
pauseCounter = 0

while True:
    program = w.GetWindowText(w.GetForegroundWindow()).strip()
    check_pause()
    if program == 'Epic Perfect World' and not pause:
        if count >= 30:
            depositToBank()
            count = 0
            invalidCount = 0
            flyToCrystals()
        print("Attempting to find target")
        press('tab')
        start = time.time()
        if valid_target():
            invalidCount = 0
            while valid_target():
                print("LOCKED ON!")
                press('1')
                time.sleep(.5)
                end = time.time()
                if end - start > 15:
                    press('2')
                    time.sleep(.5)
                    invalidCount = invalidCount + 1
                    break
            press('7')
            time.sleep(.2)
            press('7')
            time.sleep(.2)
            press('7')
            time.sleep(.2)
            count = count + 1
        elif find_target() == "Wood Dummy":
            count = 0
            invalidCount = 0
            flyToCrystals()
        else:
            invalidCount = invalidCount + 1

        if invalidCount > 10:
            invalidCount = 0
            flyToCrystals()
    else:
        print("PWI not on screen or script paused")
        time.sleep(10)

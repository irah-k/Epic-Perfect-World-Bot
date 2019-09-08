import time
import ctypes
import pytesseract
import win32gui

import pyautogui
from pyautogui import press
from PIL import ImageGrab
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
# print(pytesseract.image_to_string(Image.open('temp.png'), config='--psm 7'))

while True:
    print(pyautogui.position())
    time.sleep(2)

# time.sleep(10)
# pyautogui.click(1750, 248)  # open coordinate
# time.sleep(.2)
# pyautogui.doubleClick(474, 126)  # click crystals on coordinate
# time.sleep(30)
# press('esc')
import pyautogui as pag
import random
import time

while True:
    x = random.randint(100, 1000)
    y = random.randint(100, 1000)
    pag.moveTo(x, x, 0.5)
    time.sleep(4)

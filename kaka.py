import pyautogui as py
import time
import os


py.press('win')
time.sleep(1)
py.write("google")
time.sleep(1)
py.press("enter")
time.sleep(1)
py.write("https://www.youtube.com/shorts/QvXGlD9qhjA")
time.sleep(1)
py.press("enter")
time.sleep(1)
py.press("search")
time.sleep(1)
py.write("")
py.press("enter")

os.system("pause")

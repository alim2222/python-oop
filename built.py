import time
import random
import cv2
import math
import pyautogui
#time.sleep(2)
print("Start")
fruits=["kamal", "jamal", "alim", "rofik"]
#time.sleep(5)
print(random.choice(fruits))
print(random.randint(2,8))
print(math.sin(0))
print(math.cos(0))
print(math.cos(45))
print(math.pi)
print(math.e)
print(math.ceil(2.4))
print(math.floor(2.4))
print(math.sqrt(16))
print(math.pow(2, 4))
from time import sleep
sleep(5)
for i in range (1, 5):
    pyautogui.write(" I Love You", interval=0.1)
    pyautogui.press("enter")

cam=cv2.videocpture(2)
while True:
    _, frame=cam.red()
    cv2.imshow("my cam",frame)
    cv2.waitkey(2)
import pyautogui as pag
import cv2 as cv
import time
import numpy as np
import keyboard

pag.PAUSE = 0.001
keyboard.wait('q')
while True:
    if keyboard.is_pressed('esc'):
        break

    if keyboard.is_pressed('w'):
        time.sleep(2)

    img = pag.screenshot(region=(743,420, 451,490))
    img = np.array(img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite('grayscaled.jpg', gray)
    time.sleep(0.01)

    image = cv.imread('grayscaled.jpg', cv.IMREAD_GRAYSCALE)

    min_x_loc = cv.minMaxLoc(image)[2][0]
    min_y_loc = cv.minMaxLoc(image)[2][1]

    if cv.minMaxLoc(image)[0] < 30:
        pag.moveTo(min_x_loc+790, min_y_loc+460)
        pag.mouseDown()
        pag.mouseUp()
    else:
        pass

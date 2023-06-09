import cv2
import pyautogui
import time
import numpy as np
import os
templates = os.listdir('templates')
def read():
    file = pyautogui.screenshot(region=(550,200, 600, 250))
    x_val = []
    numbers = []
    img_rgb = cv2.cvtColor(np.array(file), cv2.COLOR_RGB2BGR)
    for i in range(len(templates)): # Identify numbers
        template = cv2.imread("templates\\"+str(i)+'.png')

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = .8
        loc = np.where(res >= threshold)
        if (loc[::-1])[0].size and (loc[::-1][1]).size > 4:
            print(i)
            x_val.append(np.array(loc[::-1][0]).tolist())
            numbers.append(i)
    print(x_val)
    print(numbers)

    for i in x_val:
        x_val[x_val.index(i)] = max(i)

    Z = [x for _,x in sorted(zip(x_val,numbers))]
    print(x_val)
    if len(Z) == 1:
        pyautogui.write(str(Z[0]*2),interval=0)
    else:
        pyautogui.write(str(Z[0]+Z[1]),interval=0)
time.sleep(2)
    
while True:
    read()
    pyautogui.press("enter")
import cv2
import pyautogui
import time
import numpy as np
import os
templates = os.listdir('templates')
print(templates)
def read():
    file = pyautogui.screenshot(region=(550,200, 600, 250))
    x_val = []
    numbers = []
    img_rgb = cv2.cvtColor(np.array(file), cv2.COLOR_RGB2BGR)
    for i in templates: # Identify numbers
        template = cv2.imread('templates\\'+i)

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = .8
        loc = np.where(res >= threshold)
        if (loc[::-1])[0].size and (loc[::-1][1]).size > 4:
            x_val.append(np.array(loc[::-1][0]).tolist())
            numbers.append(os.path.splitext(i)[0])
    for i in x_val:
        if type(i) == int:
            pass
        else:
            if max(i) - min(i) > 50:
                numbers.append(numbers[x_val.index(i)])
                x_val[x_val.index(i)] = max(i)
                x_val.append(min(i))
            else:
                x_val[x_val.index(i)] = max(i)
    print(x_val)
    Z = [x for _,x in sorted(zip(x_val,numbers))]
    print(Z)
    pyautogui.write(str(eval(str(''.join(Z)))),interval=0)

time.sleep(2)
    
while True:
    read()
    pyautogui.press("enter")
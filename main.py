import cv2
import pyautogui
import time
import numpy as np
def read():
    file = pyautogui.screenshot(region=(550,200, 600, 250))
    x_val = []
    numbers = []
    img_rgb = cv2.cvtColor(np.array(file), cv2.COLOR_RGB2BGR)
    for i in range(10): # Identify numbers
        template = cv2.imread("templates\\"+str(i)+'.png')

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = .8
        loc = np.where(res >= threshold)
        w, h = template.shape[:-1]
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        if (loc[::-1])[0].size and (loc[::-1][1]).size > 4:
            print(i)
            x_val.append(np.array(loc[::-1][0]).tolist())
            numbers.append(i)
    cv2.imwrite('result.png', img_rgb)
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



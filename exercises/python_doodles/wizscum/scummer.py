import time
import io

import sendkeys

import cv2
import numpy as np

import pyautogui
from PIL import Image
import pytesseract


def get_bonus():
    pytesseract.pytesseract.tesseract_cmd = r'c:\cygwin64\bin\tesseract.exe'
    # Box(left=820, top=265, width=67, height=38)
    screen_shot = pyautogui.screenshot(region=(820, 265, 67, 38))

    screen_shot = screen_shot.convert('L')
    ret, screen_shot = cv2.threshold(np.array(screen_shot), 125, 255, cv2.THRESH_BINARY)
    screen_shot = Image.fromarray(screen_shot.astype(np.uint8))
    ocr = pytesseract.image_to_string(screen_shot, config='--tessdata-dir . --psm 7 -c tessedit_char_whitelist=0123456789')
    try:
        return int(ocr)
    except ValueError:
        return 0


def main():

    pyautogui.FAILSAFE = True
    pyautogui.click(839, 596)
    while True:
        sendkeys.PressKey(sendkeys.VK_Z)
        time.sleep(.1)
        sendkeys.ReleaseKey(sendkeys.VK_Z)
        time.sleep(1.2)
        bonus = get_bonus()
        print(bonus)
        if bonus >= 30:
            print('FOUND!!!')
            break
        else:
            sendkeys.PressKey(sendkeys.VK_ESC)
            time.sleep(.1)
            sendkeys.ReleaseKey(sendkeys.VK_ESC)
            time.sleep(.4)


if __name__ == '__main__':
    main()
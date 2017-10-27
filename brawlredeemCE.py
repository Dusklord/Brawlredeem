import pyautogui
import itertools
import time
import random

chars = list('ABCDEFGHJKLMNOPQRSTUVWXYZ' + '123456789')

input("Hit <Enter> to launch the program...")

#Opening the store and the "redeem a code" popup
pyautogui.moveTo(500, 900)
pyautogui.click()
pyautogui.moveTo(250, 1000)
pyautogui.click()

try:
    while True:
        random.shuffle(chars)
        
        for comb in itertools.permutations(chars, 12):

            time.sleep(0.05)

            pyautogui.moveTo(720, 350)
            pyautogui.click()

            #Cleaning the previous code
            for i in range(13):
                pyautogui.press('del')

            #A code is like XXXXXX-XXXXXX
            toWrite = ''.join(comb[:6]) + "-" + ''.join(comb[6:])
            pyautogui.typewrite(toWrite)
            
            pyautogui.moveTo(950, 450)
            pyautogui.click()
            
            time.sleep(1.6)
            
            pyautogui.moveTo(950, 600)
            pyautogui.click()
            break
        
except KeyboardInterrupt:
    exit()

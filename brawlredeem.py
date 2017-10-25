import pyautogui
import itertools
import time
import random
import string
import pickle

chars = list(string.ascii_uppercase + "0123456789")
tested_codes = []

with open('tested_codes.txt', 'rb') as file:
    tested_codes = pickle.load(file)

try:
    while 1:
        random.shuffle(chars)
        
        for comb in itertools.permutations(chars, 13):
            
            if comb in tested_codes:
                continue
                
            tested_codes.append(comb)

            pyautogui.moveTo(700, 350)
            pyautogui.click()

            for i in range(15):
                pyautogui.press('del')

            pyautogui.typewrite(comb[:6])
            pyautogui.typewrite("-")
            pyautogui.typewrite(comb[7:])
            
            pyautogui.moveTo(950, 450)
            pyautogui.click()
            
            time.sleep(5)
            
            pyautogui.moveTo(950, 600)
            pyautogui.click()
            break
        
except KeyboardInterrupt:
    with open('tested_codes.txt', 'ab') as file:
        pickle.dump(tested_codes, file)

    print("Fermeture du programme en cours...")
    exit()


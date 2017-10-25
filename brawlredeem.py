import pyautogui
import itertools
import time
import random
import string
import pickle

chars = list(string.ascii_uppercase + "0123456789")
tested_codes = []

try:
    with open('tested_codes.txt', 'rb') as file:
        tested_codes = pickle.load(file)

except FileNotFoundError:
    pass

input("Hit <Enter> to launch the program...")

#Opening the store and the "redeem a code" popup
pyautogui.moveTo(500, 900)
pyautogui.click()
pyautogui.moveTo(250, 1000)
pyautogui.click()

i = 0

try:
    while i < 1000:
        i += 1
        random.shuffle(chars)
        
        for comb in itertools.permutations(chars, 13):
            
            if comb in tested_codes:
                continue
                
            tested_codes.append(comb)

            time.sleep(0.5)

            pyautogui.moveTo(720, 350)
            pyautogui.click()

            #Cleaning the previous code
            for i in range(15):
                pyautogui.press('del')

            #A code is like XXXXXX-XXXXXX
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

with open('tested_codes.txt', 'ab') as file:
    pickle.dump(tested_codes, file)
    print("Fermeture du programme en cours...")
    exit()

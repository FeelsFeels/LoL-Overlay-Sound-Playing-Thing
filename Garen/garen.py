import pyautogui
import time
import keyboard
import pygame
from pygame import mixer
from msvcrt import getch

mixer.init()
mixer.music.load('garen.mp3')

class GarenCDs:
    canUseE = False

garen = GarenCDs()


def checkscreen():
    e_up = pyautogui.locateOnScreen('garen_E_up.png', region=(784, 975, 200, 53), confidence=0.8)
    e_spinning = pyautogui.locateOnScreen('garen_E_spinning.png', region=(784, 975, 200, 53), confidence=0.7)

    if e_up:
        ## Edge case, false positive:
        ##Sometimes launches on level up
        if not garen.canUseE:
            mixer.music.stop()
        garen.canUseE = True
        
    ## If not None
    if not e_up and garen.canUseE:
        garen.canUseE = False
        print('Garen E is used')
        mixer.music.play()
        time.sleep(1)
        while True:
            time.sleep(0.1)
            e_spinning = pyautogui.locateOnScreen('garen_E_spinning.png', region=(784, 975, 200, 53), confidence=0.7)
            if not e_spinning:
                mixer.music.stop()
                break

    

while True:
    time.sleep(0.1)
    checkscreen()


# while True:
#     time.sleep(10)
#     pyautogui.locateOnScreen('garen_E_up.png', region=(784, 975, 200, 53), confidence=0.8)





# ingame
# 784, 975, 

# //983, 975//

# 784, 1028

# width = 200 
# height = 53
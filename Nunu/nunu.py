import pyautogui
import time
import keyboard
import pygame
from pygame import mixer
from msvcrt import getch

mixer.init()
mixer.music.load('nunu.mp3')

class ChampCDs:
    abilityAvailable = False

nunu = ChampCDs()


def checkscreen():
    channelling = pyautogui.locateOnScreen('nunu_channelling.png', region=(871, 778, 184, 9), confidence=0.7)

    if channelling:
        print('Deja Vu')
        mixer.music.play()
        time.sleep(0.3)
        while True:
            # time.sleep(0.05)
            channelling = pyautogui.locateOnScreen('nunu_channelling.png', region=(871, 778, 184, 9), confidence=0.7)
            if not channelling:
                mixer.music.stop()
                break

    

while True:
    time.sleep(0.1)
    checkscreen()


# while True:
#     time.sleep(10)
#     pyautogui.locateOnScreen('garen_E_up.png', region=(784, 975, 200, 53), confidence=0.8)





# ingame
# x 871   1054
# y 778   786
# w 183
# h 8
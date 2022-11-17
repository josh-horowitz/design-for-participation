import webbrowser
import serial
import pyautogui
import time

arduino = serial.Serial(port='COM4', baudrate = 9600, timeout=0.1)
cupSet = True
start = 0
restart = False
inactive = False

while True:
    read = arduino.readline()
    # print(read)
    print(f'Start: {time.time() -   start}, cupSet: {cupSet}, inactive: {inactive}')
    if read == b'CUP SET\r\n':
        if (cupSet==True):
            cupSet = False
            inactive = False
            # webbrowser.open('https://www.youtube.com/watch?v=le6vodQGeVI&t=384s')
            if restart:
                pyautogui.press('n')
                restart = False
            pyautogui.press('space')
        #  playsound('pouring.mp3')
        else: 
            cupSet = True
            pyautogui.press('space')
            start = time.time()
            inactive = True
    if time.time() - start > 10 and cupSet == True and inactive == True:
        pyautogui.press('n')
        restart = True
        inactive = False

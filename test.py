import webbrowser
import serial
import pyautogui
import time

arduino = serial.Serial(port='COM3', baudrate = 9600, timeout=0.1)
cupSet = True
start = 0

while True:
    read = arduino.readline()
    print(read)
    if read == b'CUP SET\r\n':
        if (cupSet==True):
            cupSet = False
            # webbrowser.open('https://www.youtube.com/watch?v=le6vodQGeVI&t=384s')
            pyautogui.press('space')
        #  playsound('pouring.mp3')
        else: 
            cupSet = True
            pyautogui.press('space')
            start = time.time()
    if time.time() - start > 10000:
        pyautogui.press('p')

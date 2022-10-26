import webbrowser
import serial
from playsound import playsound
import pyautogui
import time

arduino = serial.Serial(port='/dev/tty.usbmodem142101', baudrate = 9600, timeout=0.1)
cupSet = True

while True:
    read = arduino.readline()
    print(read)
    if read == b'CUP SET\r\n':
        if (cupSet==True):
            cupSet = False
            webbrowser.open('https://www.youtube.com/watch?v=le6vodQGeVI&t=384s')
            pyautogui.press('space')
        #  playsound('pouring.mp3')
        else: 
            cupSet = True
            # pyautogui.press('space')    
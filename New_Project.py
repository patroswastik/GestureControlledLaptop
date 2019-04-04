import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('com5',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print incoming
    
    if 'Left Arrow' in incoming:
        pyautogui.press('left')

    if 'Right Arrow' in incoming:
        pyautogui.press('left')  

    if 'BackSpace' in incoming:
        pyautogui.press('backspace') 

    if 'Caps' in incoming:
        pyautogui.press('capslock')
    if 'ABC' in incoming:
        pyautogui.typewrite('a')
        pyautogui.typewrite('b')
        pyautogui.typewrite('c')
    if 'DEF' in incoming:
        pyautogui.typewrite('d')
        pyautogui.typewrite('e')
        pyautogui.typewrite('f')
    if 'GHI' in incoming:
        pyautogui.typewrite('g')
        pyautogui.typewrite('h')
        pyautogui.typewrite('i')
    if 'JKLM' in incoming:
        pyautogui.typewrite('j')
        pyautogui.typewrite('k')
        pyautogui.typewrite('l')
        pyautogui.typewrite('m')
    if 'NOP' in incoming:
        pyautogui.typewrite('n')
        pyautogui.typewrite('o')
        pyautogui.typewrite('p')
    if 'QRS' in incoming:
        pyautogui.typewrite('q')
        pyautogui.typewrite('r')
        pyautogui.typewrite('s')
    if 'TUV' in incoming:
        pyautogui.typewrite('t')
        pyautogui.typewrite('u')
        pyautogui.typewrite('v')
    if 'WXYZ' in incoming:
        pyautogui.typewrite('w')
        pyautogui.typewrite('x')
        pyautogui.typewrite('y')
        pyautogui.typewrite('z')
    incoming = ""  

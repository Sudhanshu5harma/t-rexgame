import serial
import pyautogui
#from pykeyboard import PyKeyboard

#k = PyKeyboard()
ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
    p = ser.readline()
    print p
    if (p[:4] == 'jump'):
        print "working"
        pyautogui.press('space')
        #k.tap_key(k.space_key)
    else:
        print "its on else loop"

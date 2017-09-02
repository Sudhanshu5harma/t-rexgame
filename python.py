import serial
from pymouse import PyMouse
from pykeyboard import PyKeyboard

k = PyKeyboard()

ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
    print ser.readline()

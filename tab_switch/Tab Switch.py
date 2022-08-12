import serial   #Serial imported for Serial communication
import time     #Required to use delay functions
import ctypes

ser = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)
print("connection established")
while 1:
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        print(string)
        if "switch" in string:
            ctypes.windll.user32.keybd_event(0x12, 0, 0, 0) #Alt
            ctypes.windll.user32.keybd_event(0x09, 0, 0, 0) #Tab
            ctypes.windll.user32.keybd_event(0x09, 0, 2, 0) #~Tab
            ctypes.windll.user32.keybd_event(0x12, 0, 2, 0) #~Alt
            print("tab switched")

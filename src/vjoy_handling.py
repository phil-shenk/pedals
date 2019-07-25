import pyvjoy
import serial
import time

#print(pyvjoy.__file__)

MAX_VJOY = 32767

arduino = serial.Serial('COM15', 9600, timeout=.1)

j = pyvjoy.VJoyDevice(1)

#so i think EITHER set_axis OR {data.wAxisY && update} work
def play_function(X, Y, dank):
    #j.update()
    #j.data.wAxisX = int((X/1024.0) * MAX_VJOY)
    #j.data.wAxisY = int((Y/1024.0) * MAX_VJOY)
	#j.update()
    j.set_axis(pyvjoy.HID_USAGE_X, int((X/1024.0) * MAX_VJOY))
    j.set_axis(pyvjoy.HID_USAGE_Y, int((Y/1024.0) * MAX_VJOY))

   
#play_function(0,0,0)
running =True
while running:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        print data
        play_function(int(data), int(data), 1)
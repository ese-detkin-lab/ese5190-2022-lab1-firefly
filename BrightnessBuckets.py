#Ex 4.4 This code implements the combined functionality of Keyboard interface and colour measurement of apds9960

#importing all required libraries
import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960
import random


#Wiring Up connections and objects

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard) 

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
apds = APDS9960(i2c)
apds.enable_color = True
apds.color_integration_time = 64
time.sleep(5)  # Sleep for a bit to avoid a race condition on some systems

#Continously ran loop
while True:
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    
    if(c<10000):
        keyboard_layout.write("\nDim")
        
    elif(c>10000 and c<20000):
        keyboard_layout.write("\nBright")
    elif(c>20000 and c<35000):
        keyboard_layout.write("\nBrighter") 
    elif(c>35000 and c<50000):
        keyboard_layout.write("\nBrightest")
    elif(c>50000 and c<65000):
        keyboard_layout.write("\nBurnt Retinas")
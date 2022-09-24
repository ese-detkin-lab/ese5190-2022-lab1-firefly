import board
from adafruit_apds9960.apds9960 import APDS9960
import busio
import time
import random
import usb_hid
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keyboard import Keyboard

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
apds.enable_proximity = True
apds.enable_gesture = True

def roll():			  	                   #Function to generate dice values
    val=random.randint(1,6)
    keyboard_layout.write(str(val))	       #Write the dice value on screen
    print(val)

while True:
    prox = apds.proximity
    if prox>3:
        print("Roll")
        roll()
        while prox>1:                       #waits for the hand to be moved to avoid multiple rolling at a time
            prox = apds.proximity

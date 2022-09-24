# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries

# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Keyboard example"""
import time
import board
import digitalio
import usb_hid
import busio
import neopixel
import analogio
import adafruit_apds9960.apds9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.mouse import Mouse

# The keyboard object!
time.sleep(0.01)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)


i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = False
apds.enable_color = True
mouse = Mouse(usb_hid.devices)

select = digitalio.DigitalInOut(board.A2)
select.direction = digitalio.Direction.INPUT
select.pull = digitalio.Pull.UP
sensor.color_integration_time = 1 
# the 'clear' value of natural brightness
r, g, b, c = sensor.color_data 
ct = c
while True:
    r, g, b, c = sensor.color_data
    #print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    if c > ct:    
        keyboard.press(Keycode.O)
        keyboard.release_all()
        print(c,ct)
        ct=c
    elif c < ct:  
        keyboard.press(Keycode.BACKSPACE)
        keyboard.release_all()
        print(c,ct)
        ct = c
    else:
        pass
    
    time.sleep(0.1)

# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Keyboard example"""
import time

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import adafruit_apds9960.apds9960
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=True)

# A simple neat keyboard demo in CircuitPython

# The Keycode sent for each button, will be paired with a control key
keys_pressed = [Keycode.BACKSPACE, "O"]
control_key = Keycode.SHIFT

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_color = True
sensor.enable_gesture = True
 
sensor.color_integration_time = 1

print("Waiting for key pin...")

prev_brightness = 0

while True:
    r, b, g, c = sensor.color_data
    
    gesture = sensor.gesture()
    
    if c >= prev_brightness:
        keyboard_layout.write("Getting Brighter!")
        
    else:
        keyboard_layout.write("Getting Dimmer!")

    
    if gesture == 0x01:
        print("up")
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:
        print("left")
    elif gesture == 0x04:
        print("right")
    
    prev_brightness = c
    time.sleep(0.5)

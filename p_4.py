# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Blink example for boards with ONLY a NeoPixel LED (e.g. without a built-in red LED).
Includes QT Py and various Trinkeys.
Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy
Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel
import busio
from adafruit_apds9960.apds9960 import APDS9960
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

def keyboard_helper(key):
    control_key = Keycode.BACKSPACE
    if isinstance(key, str):  # If it's a string...
        keyboard_layout.write(key)  # ...Print the string
    else:  # If it's not a string...
        keyboard.press(control_key, key)  # "Press"...
        keyboard.release_all()  # ..."Release"!

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

#print("Hello World!")

i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)
apds.enable_color = True
apds.color_integration_time = 50

keys_pressed = [Keycode.O]
control_key = Keycode.BACKSPACE

# The keyboard object!
time.sleep(1)
# Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

prev_c = 0
safe_value = 200
while True:
    r, g, b, c = apds.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}, prev_c: {4}'.format(r, g, b, c, prev_c))

    key = keys_pressed[0]

    if c > 300:
        if c <= prev_c - safe_value:
            keyboard.send(control_key)
            prev_c = c
        elif c >= prev_c + safe_value:
            keyboard.send(key)
            prev_c = c
        else:
            continue
    else:
        prev_c = 0

    time.sleep(0.1)
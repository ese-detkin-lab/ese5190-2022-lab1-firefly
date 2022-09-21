# Lab1 Section 4.4
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

import neopixel
import busio
import adafruit_apds9960.apds9960

from adafruit_apds9960.apds9960 import APDS9960
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
apds.color_integration_time = 10

keypress_pins = [board.A1, board.A2]
key_pin_array = []
color_key = ["Red:", "Green:", "Blue:", "Clear:"]

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

count = 0
irange = [0,1,2,3]
while count < 20:
    for i in irange:
        r, g, b, c = apds.color_data
        values = [r,g,b,c]
        color = color_key[i]  # Get the corresponding Keycode or string
        intensity = str(values[i])
        print(color+ str(intensity))
        keyboard_layout.write(color)  # ...Print the string
        keyboard_layout.write(intensity)
        keyboard_layout.write("   ")
        keyboard.release_all()
    keyboard_layout.write("\n")

    time.sleep(1)
    count += 1

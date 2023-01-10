# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Keyboard example"""
import time
import neopixel
import board
import digitalio
import usb_hid
import busio
import adafruit_apds9960.apds9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

pixels = neopixel.NeoPixel(baord.NeoPixel, 1)
aps.enable_color = true
apds.color_integration_time = 10

# A simple neat keyboard demo in CircuitPython

keys_pressed = [Keycode.O, Keycode.BACKSPACE]

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True

while sensor.enable_color == True:

    r, g, b, c = aps.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))

    if c > 300:
        keyboard_layout.write("Sun\n")
        pixels.fill(0, 255, 0)//Green
    elif c < 100:
        keyboard_layout.write("Dark\n")
        pixels.fill(250,0,0)//Red
    else:
        keyboard_layout.write("\n")

    time.sleep(0.1)

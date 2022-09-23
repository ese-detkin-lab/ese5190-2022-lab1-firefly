# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Mouse example"""
import time
import board
import usb_hid
import adafruit_apds9960.apds9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# The Keycode sent for each button, will be paired with a control key
keys_pressed = [Keycode.O, "\b", Keycode.L, Keycode.S]
control_key = Keycode.SHIFT

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.color_integration_time = 10

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

sensor.enable_color = True
brightness = 0
red = 0
while True:
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    if c < brightness:
        # print(steps(x))
        keyboard_layout.write(keys_pressed[1])
        brightness = c
    elif c > brightness:
        keyboard.press(keys_pressed[0])
        keyboard.release_all()
        brightness = c
    time.sleep(0.05)

    if r < red:
        # print(steps(x))
        keyboard.press(control_key, keys_pressed[2])
        keyboard.release_all()
        red = r
    elif r > red:
        keyboard.press(control_key, keys_pressed[3])
        keyboard.release_all()
        red = r
    time.sleep(0.05)

    if g > 1500:
        break




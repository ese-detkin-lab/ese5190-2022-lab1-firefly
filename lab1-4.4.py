
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Mouse example"""
import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
import busio
import adafruit_apds9960.apds9960
import neopixel

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_color = True
sensor.enable_gesture = True
sensor.color_integration_time = 72   #make the keyboard press slower

#mouse = Mouse(usb_hid.devices)
# Our array of key objects
key_pin_array = []
# The Keycode sent for each button, will be paired with a control key
#keys_pressed = [Keycode.o, "\b"]
control_key = Keycode.SHIFT

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

while True:
    r, g, b, c = sensor.color_data
    print(g)
#use keyboard library
    if r > 250:
        keyboard.press(Keycode.R)  # press g
        keyboard.release_all()
    elif g > 80:
        keyboard.press(Keycode.G)  # press g
        keyboard.release_all()
    elif c < 10:
        break
    else:
        keyboard_layout.write("\b")

    '''
    gesture = sensor.gesture()
    if gesture == 0x01:
        keyboard_layout.write("up\n")
    elif gesture == 0x02:
        keyboard_layout.write("down\n")
    elif gesture == 0x03:
        keyboard_layout.write("left\n")
    elif gesture == 0x04:
        keyboard_layout.write("right\n")
    '''

#use mouse library
'''
    if c > 30:
        # print(steps(y))
        mouse.move(y=-8)
    else:
        # print(steps(y))
        mouse.move(y=8)
 '''

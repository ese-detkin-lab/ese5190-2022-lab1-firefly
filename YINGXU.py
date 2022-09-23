# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Keyboard example"""
import time
from adafruit_apds9960.apds9960 import APDS9960
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

def handle(key):
    if isinstance(key, str):  # If it's a string...o
        keyboard.send(key)  # ...Print the string
    else:  # If it's not a string...
        keyboard.send( key)  # "Press"...
        keyboard.release_all()  # ..."Release"!oo


if __name__ =="__main__":
    i2c = board.STEMMA_I2C()
    apds = APDS9960(i2c)
    apds.color_integration_time=10
    # apds.enable_proximity = True
    apds.enable_gesture = True
    apds.enable_color=True
    bright=0
    bright_prev=0
    tolerance=250

    keys_pressed = [Keycode.O]
    control_key = Keycode.BACKSPACE

    # The keyboard object!
    time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)


    # For QT Py M0:
    # led = digitalio.DigitalInOut(board.SCK)
    # led.direction = digitalio.Direction.OUTPUT

    print("Waiting for key pin...")

    while True:
        time.sleep(1)
        _,_,_,bright=apds.color_data
        if bright>bright_prev+tolerance:
            #handle(keys_pressed[0])
            info = keyboard_layout.write("becoming brighter\n")
            time.sleep(0.3)
        elif bright<bright_prev-tolerance:
            #handle(control_key)
            info = keyboard_layout.write("becoming darker\n")
            time.sleep(0.3)
        else :
            continue
        bright_prev=bright
        print(print('{0},\t{1}'.format(bright,bright_prev)))
        time.sleep(0.01)

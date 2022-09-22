# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Keyboard example"""
import time

import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
from adafruit_apds9960.apds9960 import APDS9960
import neopixel



# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on ome systems

# enable color show
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

# enable I2c
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)

# enable sensor
apds.enable_color = True
apds.enable_proximity = True
apds.enable_gesture = True
apds.color_integration_time = 150

# define keyboard (hid)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# define mouse
mouse = Mouse(usb_hid.devices)


while True:
    # # use distance print alphabet
    dis = apds.proximity
    if dis > 100 and dis <= 210:
        print('distance is:', dis)
        keyboard.send(Keycode.A)
    if dis > 210 and dis <= 220:
        keyboard.send(Keycode.SHIFT, Keycode.B)
        print('distance is:', dis)

    # use ambient light print sentence
    # test it on the totally dark place
    r, g, b, c = apds.color_data
    clear = c / 256
    pixels.fill((clear, clear, clear))
    if clear <2 :
        print("clear: ", clear)
        keyboard_layout.write('It is too dim, please turn on the light!\n')

    # use gesture move mouse
    gesture = apds.gesture()
    if gesture == 1:
        mouse.move(y=80)
        print('Saw gesture: up')
    if gesture == 2:
        mouse.move(y=-80)
        print('Saw gesture: down')
    if gesture == 3:
        mouse.move(x=80)
        print('Saw gesture: left')
    if gesture == 4:
        mouse.move(x=-80)
        print('Saw gesture: right')

    # stop when i = 20
    if clear > 220:
        print('System turn off')
        break
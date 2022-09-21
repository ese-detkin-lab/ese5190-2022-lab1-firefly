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

# define keyboard (hid)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# define mouse
mouse = Mouse(usb_hid.devices)


while True:
    # # use distance print alphabet
    dis = apds.proximity
    if dis > 180 and dis <= 210:
        print('distance is:', dis)
        keyboard.send(Keycode.A)
    if dis > 210 and dis <= 220:
        keyboard.send(Keycode.SHIFT, Keycode.B)
        print('distance is:', dis)

    # use ambient light print sentence
    # test it on the totally dark place
    r, g, b, c = apds.color_data
    red = r * 255 / 65535
    green = g * 255 / 65535
    blue = b * 255 /65535
    pixels.fill((red, green, blue))
    if red > 100 :
        print("red: ", red, " green: ", green, " blue: ", blue)
        keyboard_layout.write('warm light\n')
    elif green > 100:
        print("red: ", red, " green: ", green, " blue: ", blue)
        keyboard_layout.write('color of sping\n')
    elif blue > 100:
        print("red: ", red, " green: ", green, " blue: ", blue)
        keyboard_layout.write('color of winter\n')

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
    if red > 200:
        break
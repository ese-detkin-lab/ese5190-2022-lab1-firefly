import time
import neopixel
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import board
from adafruit_apds9960.apds9960 import APDS9960
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
i2c = board.STEMMA_I2C()
kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True
apds.enable_color = True
# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
fault_tolerance = 20
while True:
    #gesture = apds.gesture()
    r1, g1, b1, c1 = apds.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r1/255, g1, b1, c1))
    pixels.fill((r1/255, g1, b1, c1))
    time.sleep(4)
    r2, g2, b2, c2 = apds.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r2, g2, b2, c2))
    pixels.fill((r2/255, g2, b2, c2))
    if r1 + g1 + b1 + c1 > r2 + g2 + b2 + c2 + fault_tolerance:
        kbd.send(Keycode.BACKSPACE)
        print("A")
    elif r1 + g1 + b1 + c1 < r2 + g2 + b2 + c2 + fault_tolerance:
        keyboard_layout.write("o")
        #kbd.send(Keycode.O)
        print ("C")
    else:
        print("No action!")
        #continue
    kbd.release_all
    r3, g3, b3, c3 = apds.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r3/255, g3, b3, c3))
    pixels.fill((r3/255, g3, b3, c3))
    if r3 + g3 + b3 + c3 < 50:
        print("Test is over!")
        break


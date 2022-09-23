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
#fault_tolerance = 20
while True:
    r, g, b, c = apds.color_data
    gesture = apds.gesture()
    if gesture == 0x01:
        a = keyboard_layout.write('On!\n')
        pixels.fill((r + 255, 0, 0, 0))
        time.sleep(1)
        print("up")
    elif gesture == 0x02:
        a = keyboard_layout.write('Back!\n')
        pixels.fill((0, g + 255, 0, 0))
        time.sleep(1)
        print("down")
    elif gesture == 0x03:
        a = keyboard_layout.write('Turn Left!\n')
        pixels.fill((0, 0, b + 255, 0))
        time.sleep(1)
        print("left")
    elif gesture == 0x04:
        a = keyboard_layout.write('Turn Right!\n')
        pixels.fill((r, g, b, c ))
        time.sleep(1)
        print("right")


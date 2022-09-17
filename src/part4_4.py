# Manipulate the keyboard.
# Type 'o' when brightness increases, and send a 'backspace' command when the brightness decreases.
# The LED is red when proximity is less than 200 and green if greater than 200.
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time
import board
from adafruit_apds9960.apds9960 import APDS9960

import neopixel

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
kbd = Keyboard(usb_hid.devices)
apds.enable_proximity = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
keyboard_layout = KeyboardLayoutUS(kbd)

preProximity = apds.proximity
while True:

    time.sleep(0.1)
    curProximity = apds.proximity
    print(curProximity)

    if curProximity < 200:
        if curProximity > preProximity:
            keyboard_layout.write("Get close\n")
            pixels.fill((255, 255, 0))
        else if (curProximity < preProximity):
            keyboard_layout.write("Get further\n")
            pixels.fill((0, 255, 0))
    else:
        keyboard_layout.write("Need to stop!\n")
        pixels.fill((255, 0, 0))       

    preProximity = curProximity

# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Blink example for boards with ONLY a NeoPixel LED (e.g. without a built-in red LED).
Includes QT Py and various Trinkeys.
Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy
Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel
import busio
from adafruit_apds9960.apds9960 import APDS9960

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

#print("Hello World!")

i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)
#apds.enable_proximity = True
#apds.enable_gesture = True
apds.enable_color = True
apds.color_integration_time = 50

TH = 32
while True:
    # pixels.fill((255, 0, 0))
    # time.sleep(0.5)
    # pixels.fill((0, 0, 0))
    # time.sleep(0.5)

    # gesture = apds.gesture()
    # print(apds.proximity)

    r, g, b, c = apds.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    color_value = min(c/TH, 255)
    pixels.fill((color_value, 0, 0))
    time.sleep(0.0001)

    # gesture == 0x01:
    #     print("up")
    # elif gesture == 0x02:
    #     print("down")
    # elif gesture == 0x03:
    #     print("left")
    # elif gesture == 0x04:
    #     print("right")
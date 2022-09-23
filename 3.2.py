import time
import neopixel
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import board
from adafruit_apds9960.apds9960 import APDS9960
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True
apds.enable_color = True
# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
while True:
    r, g, b, c = apds.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r/255, g/255, b/255, c/255))
    pixels.fill((r/255, g/255, b/255, c/255))



# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
import neopixel

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)


while True:
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the data and print the different channels
    r, g, b, c = apds.color_data

    pixels.fill((255 * r / 65535, 255 * g / 65535, 255 * b / 65535))
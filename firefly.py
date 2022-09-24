# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import digitalio
import time
import busio
import neopixel
import adafruit_apds9960.apds9960

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=True)

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_color = True
 
sensor.color_integration_time = 1

pixels.fill((255, 0, 0))  

while True:
    r, b, g, c = sensor.color_data
    pixels.brightness = c/4096
    pixels.show()


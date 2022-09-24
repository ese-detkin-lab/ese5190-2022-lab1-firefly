# ESE519 lab1 part3

import time
import board
import neopixel
from adafruit_apds9960.apds9960 import APDS9960

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
apds.color_integration_time = 10

while True:
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the data and print the different channels
    r, g, b, c = apds.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))

    pixels.fill((r/41, g/41, b/41))


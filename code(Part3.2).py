print("Lab 1  Part 3.2")

# blink with ambient light

import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
apds.color_integration_time = 150

while True:
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the data and print the different channels
    r, g, b, c = apds.color_data
    red = r /256
    green = g /256
    blue = b /256
    clear = c /256
    pixels.fill((0, clear, 0))
    print("red: ", red)
    print("green: ", green)
    print("blue: ", blue)
    print("clear: ", clear)

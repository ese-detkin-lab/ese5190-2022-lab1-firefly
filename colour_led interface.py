#This program takes the value of colour sensor and uses brightness measurement to change intensity of LED
import board
import busio
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960
import neopixel
import time

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.fill((0, 0, 0))
sensor.enable_color = True
while(True):
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    time.sleep(0.005)
    p = (c/65535)*255
    pixel.fill((p, p, 0))

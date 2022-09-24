import busio
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
from adafruit_apds9960.apds9960 import APDS9960

i2c = busio.I2C(board.SCL1, board.SDA1)
apds = APDS9960(i2c)

apds.enable_color = True
pixels.fill((255, 255, 255))

apds.color_integration_time = 7

while True:
    r, g, b, c = apds.color_data
    #print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    pixels.brightness = c/300.0
    time.sleep(0.07)

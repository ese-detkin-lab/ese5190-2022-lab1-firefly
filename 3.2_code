import board
import time
import busio
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

i2c = busio.I2C(board.SCL1, board.SDA1)
apds = APDS9960(i2c)
apds.enable_color = True
apds.color_integration_time = 10
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)


while True:
    r, g, b, c = apds.color_data

    if c <= 50:
        pixels.fill((0, 0, 0))
    
    else:
        pixels.fill((r, g, b))

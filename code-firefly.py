import board
from adafruit_apds9960.apds9960 import APDS9960
import neopixel

i2c = board.STEMMA_I2C()
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

apds = APDS9960(i2c)
apds.enable_color = True

apds.color_integration_time=1

while True:
    r, g, b, c = apds.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    pixels.fill((0, 0, c*30))

    
import board
import neopixel
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True

pixel = neopixel.NeoPixel(board.NEOPIXEL,1)
apds.color_integration_time = 0x1

while True:
    r, g, b, c = apds.color_data

    if c <= 32:
        pixel.fill((0,0,0))
    else:
        pixel.fill((r,g,b))
    

import imp
import time
import board
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

i2c = board.I2C()
apds = APDS9960(i2c)
apds.enable_color = True

pixel = neopixel.NeoPixel(board.NEOPIXEL,1)

while True:
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the data and print the different channels
    r, g, b, c = apds.color_data
    
    if c >= 3000:
        pixel.fill((255,255,0)) #set color which may be like the color of firfly
    
    pixel.fill((0,0,0))
    
    #time.sleep(0.5)
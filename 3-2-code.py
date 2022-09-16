import time
import board
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True

pixel = neopixel.NeoPixel(board.NEOPIXEL,1)
apds.color_integration_time=0x1
iterations=0
average=0
while True:
    # wait for color data to be ready
    # while not apds.color_data_ready:
    #     time.sleep(0.005)

    # get the data and print the different channels
    r, g, b, c = apds.color_data
    print(r,g,b,c)

    # iterations+=1
    # average=average+(1/(iterations+1))*(c-average)

    # if c>average:
    #     r,g,b=1.5*r,1.5*g,1.5*b
    # else:
    #     r,g,b=0.1*r,0.1*g,0.1*b
    
    # if c >= 50000:
    #     pixel.fill((255,255,0)) #set color which may be like the color of firfly
    if c<=32:
        pixel.fill((0,0,0))
    else:
        pixel.fill((r,g,b))
    
    #time.sleep(0.5)

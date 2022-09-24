#This program implements the Firefly functionality

#importing all required libraries
import board
import busio
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960
import neopixel
import time

#Wiring Up connections and objects
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

#Initializing values
pixel.fill((0, 0, 0))
sensor.enable_color = True
sensor.color_integration_time = 64

#Continously ran loop
while(True):
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    time.sleep(0.005)
    p = (c/65535)*255
    
    if(c>600):
        pixel.fill((p, p, 0))
    else:
        pixel.fill((0, 0, 0))
   
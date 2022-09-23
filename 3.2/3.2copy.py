import board
import neopixel
import time
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

# set the initial value to prevent the board from turning bright at the start time
a=10000000
x=10000000
y=10000000
z=10000000

while True:

    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the data and print the value of the sum
    r, g, b, c = apds.color_data
    k=a+x+y+z-r-g-b-c
    print("sum: ", k)

    time.sleep(0.001)

    if k>=100:
         pixels.fill((0, 0, 0))


    if k<100:
         pixels.fill((255, 0, 0))

    #get the value of preceding time
    a, x, y, z = apds.color_data


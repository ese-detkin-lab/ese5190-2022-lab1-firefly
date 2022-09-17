import usb_hid
from adafruit_hid.mouse import Mouse
import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
m = Mouse(usb_hid.devices)

prev = 0
while True:
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)
        
    # get the data and print the different channels
    r, g, b, c = apds.color_data
    
    m.move(x = (int)(200*(r + g + b)/65535 - prev))
    
    prev = (200*(r + g + b)/65535)
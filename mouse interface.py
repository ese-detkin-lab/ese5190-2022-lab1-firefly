#This program implements the mouse interface using apds9960
import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960

mouse = Mouse(usb_hid.devices)

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
apds = APDS9960(i2c)
apds.enable_color = True

while True:
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    time.sleep(0.005)
    p = (c/65535)
    if(p<0.5):
        mouse.move(x=-1)
    elif(p>0.5):
        mouse.move(x=1)

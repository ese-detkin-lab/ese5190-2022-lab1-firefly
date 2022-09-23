"""Section 4.2 Change cursor's position according to the change of brightness"""
import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
import busio
import adafruit_apds9960.apds9960
import neopixel

mouse = Mouse(usb_hid.devices)
i2c = busio.I2C(board.SCL1, board.SDA1)
apds = adafruit_apds9960.apds9960.APDS9960(i2c)

apds.enable_color = True
#Change the sampling rate
apds.color_integration_time = 50
#Set LED
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

def brightness_change(c0,c1):
    if c0 > c1: #brightness decrease
        return -1
    if c0 == c1: #no change
        return 0
    else: # brightness increase
        return 1

#Create a list to store past brightness
brightness_lst = [0,0,0,0]

while True:
    r, g, b, c = apds.color_data
    brightness_lst.insert(0, c)
    brightness_lst.pop(4)
    #print(brightness_lst)
    pixels.fill((c, c, c))

    # X-axis controls left and right movement
    if brightness_change(brightness_lst[0],brightness_lst[3]) == 0:
        mouse.move(x=0)
    if brightness_change(brightness_lst[0],brightness_lst[3]) == 1:
        mouse.move(x=8)
    if brightness_change(brightness_lst[0],brightness_lst[3]) == -1:
        mouse.move(x=-8)

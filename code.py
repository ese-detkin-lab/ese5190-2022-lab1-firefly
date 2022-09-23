import time

import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import busio
import adafruit_apds9960.apds9960
import time
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.color_integration_time=50
sensor.enable_color = True
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
n=0
red=0
green=0
blue=1

time.sleep(5)
while(red<1.5*(green+blue)):
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    pixels.fill((r, g, b))
    pixels.brightness = c/100
    if n<=c:
        layout.write('bright ')
    else:
        layout.write('dim ')
    n=c
    red=r
    green=g
    blue=b
    time.sleep(0.2)

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
sensor.color_integration_time=10
sensor.enable_color = True
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
r, g, b, c = sensor.color_data
n=0

time.sleep(5)
while(r<80):
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    pixels.fill((r, g, b))
    pixels.brightness = c/100
    if n<=c:
        layout.write('bright ')
    else:
        layout.write('dim ')
    n=c
    time.sleep(0.2)

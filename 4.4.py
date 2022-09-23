import board
import neopixel
import time
from adafruit_apds9960.apds9960 import APDS9960
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_color = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
kbd = Keyboard(usb_hid.devices)
bright_last = 0

while True:
    r, g, b, c = apds.color_data
    #print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r/257, g/257, b/257, c/257))
    pixels.fill((r/257, g/257, c/257))
    if c > bright_last:
        kbd.send(Keycode.O)
    if c < bright_last:
        kbd.send(Keycode.BACKSPACE)
    bright_last = c

import board
import busio
import time
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

apds.enable_color = True

# keyboard
keyb = Keyboard(usb_hid.devices)
keyb_l = KeyboardLayoutUS(keyb)

# wait, open Notepad quickly!
time.sleep(5)

b_past = 0
flag = True

while flag==True:
    r, g, b, c = apds.color_data
    # print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    b_cur = c/6000.0
    
    if r < 50: # to stop, block light to sensor
        print('Stop!')
        flag = False
    elif b_cur > b_past:
        keyb_l.write('o')
    elif b_cur < b_past:
        keyb.press(Keycode.BACKSPACE)
        keyb.release_all()
    b_past = b_cur
    time.sleep(0.07)
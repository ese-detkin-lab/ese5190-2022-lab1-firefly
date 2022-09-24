'''
This is the 4.4 code created by Rongqian Chen
'''

import time
import board
from adafruit_apds9960.apds9960 import APDS9960
import neopixel
import analogio
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

i2c = board.STEMMA_I2C()   # uses board.SCL and board.SDA
sensor = APDS9960(i2c)
sensor.enable_color = True
sensor.enable_gesture = True
sensor.enable_proximity = True
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
sensor.color_integration_time = 10
led_val = 0
mouse_val = 0
thres = 1000
c = 0
last_c = 0

while True:
    # LED brightness

    r, g, b, c = sensor.color_data
    if (c>thres):
        c = thres
    led_val = c/thres
    pixel.brightness = 0.8
    R = int(r*0.5)
    G = int(g*0.5)
    B = int(b*0.5)
    pixel.fill((R, G, B))
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    if max(r,g,b)==r:
        keyboard_layout.write("R")
    elif max(r,g,b)==g:
        keyboard_layout.write("G")
    elif max(r,g,b)==b:
        keyboard_layout.write("B")
    else:  
        keyboard_layout.write("-")
        #keyboard.send(Keycode.BACKSPACE)
    time.sleep(0.2)
    #gesture
    '''
    gesture = sensor.gesture()
    while gesture == 0:
        gesture = sensor.gesture()
    print('Saw gesture: {0}'.format(gesture))
    if gesture == 0x01:
        print("up")
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:
        print("left")
    elif gesture == 0x04:
        print("right")
    '''
    # keyboard
    '''
    if (c > last_c):
        keyboard_layout.write("o")
    else:
        keyboard.send(Keycode.BACKSPACE)
    last_c = c
    time.sleep(1)
    '''
    # mouse move mapping
    '''
    mouse_val = (int)(5*c/thres) - 2
    mouse.move(x=mouse_val)
    print(mouse_val)
    '''

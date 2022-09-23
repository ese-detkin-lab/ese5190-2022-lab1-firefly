import usb_hid
import time
import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_apds9960.apds9960 import APDS9960
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
temp = 0
layout.write('I \tL')
while True:
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    r, g, b, c = apds.color_data
    sub = c - temp
    temp = c
    print(c)
    if sub >= -100 and c > 200:
        layout.write('o')
    if sub < -100 and c > 200:
        layout.write('\b')
    if c < 200:
        layout.write('ve\t Upenn')
        kbd.release_all()
        break

# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries

# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Keyboard example"""
import time
import board
import digitalio
import usb_hid
import busio
import neopixel
import analogio
import adafruit_apds9960.apds9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.mouse import Mouse

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = False
apds.enable_color = True

mouse = Mouse(usb_hid.devices)

x_axis = analogio.AnalogIn(board.A0)
y_axis = analogio.AnalogIn(board.A1)
select = digitalio.DigitalInOut(board.A2)
select.direction = digitalio.Direction.INPUT
select.pull = digitalio.Pull.UP

while True:
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    time.sleep(0.1)
    
    if c > 45000:
        mouse.move(x=-5)
        
    if c < 1000:
        mouse.move(x=+5)

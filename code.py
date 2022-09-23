import time
import board
import neopixel
import usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
keyboard = Keyboard(usb_hid.devices)
apds.color_integration_time = 60
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)
time.sleep(1)
temp = 0
while True:
    r, g, b, c = apds.color_data
    print("Red: {0}, Green: {1}, Blue: {2}, Clear: {3}".format(r, g, b, temp))
    ctr = 150
    if c > 33:
        if c >= temp + ctr:
            print("bright increase")
            keyboard_layout.write("Brighter")
            temp = c
        elif c <= temp - ctr :
            print("bright down")
            keyboard_layout.write("Darker")
            temp = c
        else:
            print("No brightness change")
    else:
        print("It's dark, turn off.")
        keyboard_layout.write("System Off")
        break
    time.sleep(0.005)

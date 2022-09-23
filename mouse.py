#Mouse Control Part
import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
from adafruit_apds9960.apds9960 import APDS9960
import neopixel
time.sleep(1)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_gesture = True
mouse = Mouse(usb_hid.devices)
while True:
    gesture = apds.gesture()
    if gesture == 1:
        mouse.move(y=-60)
        print('Up')
    if gesture == 2:
        mouse.move(y=60)
        print('Down')
    if gesture == 3:
        mouse.move(x=-60)
        print('Left')
    if gesture == 4:
        mouse.move(x=60)
        print('Right')

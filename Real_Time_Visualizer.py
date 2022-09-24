import time
import board
import busio
from adafruit_apds9960.apds9960 import APDS9960
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

i2c = board.I2C()
apds = APDS9960(i2c)
apds.enable_color = True

keys_pressed = [Keycode.O, Keycode.BACKSPACE]
control_key = Keycode.SHIFT
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

while True:
    while not apds.color_data_ready:
        time.sleep(0.005)
    r, g, b, c = apds.color_data
    print("red: ", r)
    print("green: ", g)
    print("blue: ", b)
    print("clear: ", c)

    if b>50:
     if c>1400:
        j=0
        key = keys_pressed[j]
        if isinstance(key, str):
                keyboard_layout.write(key)
        else:
                keyboard.press(control_key, key)
                keyboard.release_all()
     else:
        j=1
        key = keys_pressed[j]
        if isinstance(key, str):
                keyboard_layout.write(key)
        else:
                keyboard.press(control_key, key)
                keyboard.release_all()




import time
import board
import digitalio
import usb_hid
import busio
import adafruit_apds9960.apds9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)


keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

keys_pressed = Keycode.O
control_key = Keycode.BACKSPACE
time.sleep(2)

sensor.enable_color = True
while True:
    r, g, b, c = sensor.color_data
    if (c >= 5500):
        keyboard.press(keys_pressed)
        time.sleep(6)
    else:    
        keyboard.press(control_key)
        keyboard.release_all()
"""Section 4.3 “O”-SCOPE"""
import time
import board
import analogio
import busio
import digitalio
import adafruit_apds9960.apds9960
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

i2c = busio.I2C(board.SCL1, board.SDA1)
apds = adafruit_apds9960.apds9960.APDS9960(i2c)

apds.enable_color = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
#Change the sampling rate
apds.color_integration_time = 50

def brightness_change(c0,c1):
    if c0 > c1: #brightness decrease
        return -1
    if c0 == c1: #no change
        return 0
    else: # brightness increase
        return 1

#Create a list to store past brightness
brightness_lst = [0,0,0,0]

#Create key list
key = Keycode.O
control_key = Keycode.SHIFT
backspace_key = Keycode.BACKSPACE

countdown = 1000
while countdown >= 0:
    countdown = countdown - 1
    #print(countdown)

    r, g, b, c = apds.color_data
    brightness_lst.insert(0, c)
    brightness_lst.pop(4)
    #print(brightness_lst)
    pixels.fill((c, c, c))

    if brightness_change(brightness_lst[0],brightness_lst[3]) == 0:
        pass
    if brightness_change(brightness_lst[0],brightness_lst[3]) == -1:
        keyboard.press(control_key, key)
        keyboard.release_all()
    if brightness_change(brightness_lst[0],brightness_lst[3]) == 1:
        keyboard.press(backspace_key)
        keyboard.release_all()

    time.sleep(0.01)

print("Time's up. Reload program.")

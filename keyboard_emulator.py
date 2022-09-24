
import digitalio
import usb_hid
import neopixel
import time
import busio
import board
import ad
controlkey = (Keycode.BACKSPACE)
pressedkey = (Keycode.O)
time.sleep(3)

sensor.enable_color = True
while True:
    r, g, b, c = sensor.color_data
    if (c >= 5500):
        keyboard.press(pressedkey)
        time.sleep(4)
    else:
        keyboard.press(controlkey)
        keyboard.release_all()

time.sleep(75)

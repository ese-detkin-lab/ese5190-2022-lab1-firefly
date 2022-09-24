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
apds.enable_gesture = True
apds.enable_color = True

mouse = Mouse(usb_hid.devices)

x_axis = analogio.AnalogIn(board.A0)
y_axis = analogio.AnalogIn(board.A1)
select = digitalio.DigitalInOut(board.A2)
select.direction = digitalio.Direction.INPUT
select.pull = digitalio.Pull.UP

# The keyboard object!
time.sleep(0.01)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

sensor.color_integration_time = 1 
while True:
    r, g, b, c = sensor.color_data
    #print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))

    gesture = apds.gesture()
    if gesture == 0x01:
        print("up")
        keyboard.press(Keycode.UP_ARROW)
        keyboard.release_all()  # ..."Release"!
    elif gesture == 0x02:
        print("down")
        keyboard.press(Keycode.DOWN_ARROW)
        keyboard.release_all()  # ..."Release"!
    elif gesture == 0x03:
        print("left")
        keyboard.press(Keycode.LEFT_ARROW)
        keyboard.release_all()  # ..."Release"!
    elif gesture == 0x04:
        print("right")
        keyboard.press(Keycode.RIGHT_ARROW)
        keyboard.release_all()  # ..."Release"!

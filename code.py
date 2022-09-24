# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Mouse example"""
import time
import analogio
import board
import digitalio
import usb_hid
import busio
import time
import neopixel
import adafruit_apds9960.apds9960
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

#mouse = Mouse(usb_hid.devices)
i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_color = True
sensor.enable_gesture = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
sensor.color_integration_time = 50
key="So dark! I am so scare!!!\n"
key1 =  "dim!\n"
key2="lighter now!\n"
key3="My eyes!!!My eyes!!!!?\n"
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)
gesture = sensor.gesture()
print(keyboard.led_on(Keyboard.LED_CAPS_LOCK))

last=""
while True:
    """
    x = get_voltage(x_axis)
    y = get_voltage(y_axis)
    """
    r, g, b, c = sensor.color_data

    if(c < 500 and last !=key ):
        last=key
        keyboard_layout.write(key)
    elif (c > 500 and c<1500 and last!=key1):
        last=key1
        keyboard_layout.write(key1)
    elif (c > 1500 and c<2500 and last!=key2):
        last=key2
        keyboard_layout.write(key2)
    elif (c > 2500 and last!=key3):
        last=key3
        keyboard_layout.write(last)
    #cLast = c

    #print(c)






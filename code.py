import time
import board
import busio
import digitalio
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import adafruit_apds9960.apds9960
i2c = busio.I2C(board.SCL1, board.SDA1)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.color_integration_time = 50
sensor.enable_color = True

keys_pressed = ["Game Start\nMission: Changes the brightness variation trend received by the sensor for 6 times.\n", "Now, Get Brighter!  ", "Now, Get Darker!  ", "Done\n", "Mission Success!\n", "\nGame Interrupted, Mission failed"]
control_key = Keycode.SHIFT

# The keyboard object!
time.sleep(3)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

cLast = 0
key = keys_pressed[0]
keyboard_layout.write(key)
time.sleep(1)
key = keys_pressed[1]
keyboard_layout.write(key)
time.sleep(1)
r, g, b, c = sensor.color_data
cLast = c
i = 0
while True:
    r, g, b, c = sensor.color_data
    print(c)

    if c > cLast + 100 and i % 2 == 0:
        pixels.fill((255, 255, 255))
        i = i + 1
        key = keys_pressed[3]
        keyboard_layout.write(key)
        key = keys_pressed[2]
        keyboard_layout.write(key)

    if c < cLast - 100 and i % 2 == 1:
        pixels.fill((255, 255, 255))
        i = i + 1
        key = keys_pressed[3]
        keyboard_layout.write(key)
        if i != 6:
            key = keys_pressed[1]
            keyboard_layout.write(key)
    cLast = c
    pixels.fill((0, 0, 0))
    if c < 100:
        pixels.fill((255, 0, 0))
        key = keys_pressed[5]
        keyboard_layout.write(key)
        time.sleep(1)
        break
    if i == 6:
        time.sleep(1)
        pixels.fill((0, 255, 0))
        key = keys_pressed[4]
        keyboard_layout.write(key)
        time.sleep(1)
        break
    time.sleep(0.01)

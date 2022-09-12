import time
import board
import digitalio
import analogio
import usb_hid
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
mouse=Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  

apds.enable_color = True
apds.enable_proximity=True

print(f'Current color integration time: {apds.color_integration_time}')
apds.color_integration_time=0x22
print(f'Current color integration time after changed: {apds.color_integration_time}')
current_lux=0
while True:
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the data and print the different channels
    r, g, b, c = apds.color_data
    lux=colorutility.calculate_lux(r,g,b)
    # print("red: ", r)
    # print("green: ", g)
    # print("blue: ", b)
    # print("clear: ", c)

    # print("color temp {}".format(colorutility.calculate_color_temperature(r, g, b)))
    # print("light lux {}".format(colorutility.calculate_lux(r, g, b)))
    # print("==============================\n")
    control_key = Keycode.BACKSPACE
    pixels.fill((r, g, b))
    if lux>current_lux:
        keyboard_layout.write('o')
    else:
        keyboard.press(control_key)
        keyboard.release_all()
    lux=current_lux


# TODO: Ouput the crgb value of the object in the recognized color and proximity could be used to define the interval of the output characters.
# e.g. 1 quad for proximity of 1
"""CircuitPython Essentials HID Keyboard example"""
import time
import board
import usb_hid
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# A simple neat keyboard demo in CircuitPython

# The Keycode sent for each button, will be paired with a control key
keys_pressed = [Keycode.O, Keycode.I]
control_key = Keycode.SHIFT

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)


i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Waiting for key pin...")
c_0 = 0
time.sleep(5)
while True:
    r, g, b, c_1 = apds.color_data
    diff = c_1 - c_0
    print(diff)
    print("Clear: {0}".format(c))
    led.fill((c/65535*255,0,0))
    # if the brightness increase, type the letter "o"
    if diff > 0:
        keyboard.press(control_key, keys_pressed[0])
        keyboard.release_all()
    # if the brightness decrease, type the backspace
    elif diff < 0:
        keyboard.press(control_key, keys_pressed[1])
        keyboard.release_all()
    else:
        pass

    time.sleep(0.01)
    c_0 = c_1

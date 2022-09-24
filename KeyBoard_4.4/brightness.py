import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
apds.color_integration_time=10
apds.color_gain=1

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)
control_key = Keycode.SHIFT

while True:
    r, g, b, c = apds.color_data
    lux_value = colorutility.calculate_lux(r,g,b)
    rgb=int(lux_value/4)
    print (rgb)
    #120 246 350 400
    if rgb>400:
        keyboard_layout.write("\nIt's a sunny day!")
    elif rgb>350 and rgb<400:
        keyboard_layout.write("\nIt is Brighter")
    elif rgb>250 and rgb<350:
        keyboard_layout.write("\nIt is Bright")
    elif rgb>120 and rgb<250:
        keyboard_layout.write("\nSome light at last xD")
    elif rgb<120:
        keyboard.send(Keycode.BACKSPACE)
        time.sleep(0.2)
    elif r==255:
        keyboard_layout.write("\nEmergency Exit")
        break
    

import board
import busio
import time
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

apds.enable_color = True

# keyboard
keyb = Keyboard(usb_hid.devices)
keyb_l = KeyboardLayoutUS(keyb)

# string
phrase = "Knowing he will fail, fail a thousand times, but still will not give up."
i = 0

# wait
time.sleep(5)

while i < len(phrase):
    r, g, b, c = apds.color_data
    # print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    brightness = c/6000.0
    
    if brightness > 0.5:
        pixels.fill((0, 125, 100))
        keyb_l.write(phrase[i])
        i += 1
    else:
        pixels.fill((255, 0, 125))
        keyb.press(Keycode.BACKSPACE)
        keyb.release_all()
        i -= 1
        if i < 0:
            i = 0            
    time.sleep(0.07)
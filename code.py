import time
import board
import neopixel
import analogio
import digitalio
import usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

i2c = board.STEMMA_I2C()
sensor = APDS9960(i2c)
sensor.enable_color = True
sensor.enable_gesture = True
sensor.enable_proximity = True
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
sensor.color_integration_time = 10
led_val = 0
mouse_val = 0
t = 1000
c = 0
cm=0
last_c = 0

while True:
    # LED brightness

    r, g, b, c = sensor.color_data
    if (c > t):
        c = t
    led_val = c/t
    pixel.brightness = led_val
    R = int(r)
    G = int(g)
    B = int(b)
    pixel.fill((R, G, B))
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    cm=c
    if cm>last_c:
        keyboard_layout.write("0")
    elif c<last_c:
        keyboard.send(Keycode.BACKSPACE)
    last_c=cm
    time.sleep(0.1)

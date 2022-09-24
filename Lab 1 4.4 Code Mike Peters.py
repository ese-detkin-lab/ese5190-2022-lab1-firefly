import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
import neopixel
import adafruit_apds9960.apds9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

mouse = Mouse(usb_hid.devices)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_color = True
sensor.color_integration_time = 256
#sensor.enable_gesture = True

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

c_old = 0
prox_old = 0

while True:
    r, g, b, c = sensor.color_data
    prox = sensor.proximity
    #print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    pixels.fill((c/257, c/257, c/257))
    print(sensor.proximity)
    time.sleep(0.5)

    if prox > prox_old:
        #mouse.move(x=10)
        #print(c_old)
        keyboard_layout.write('Object Closer \n')
        #time.sleep(1)
        prox_old = prox
    if prox < prox_old:
        #mouse.move(x=-10)
        #print(c_old)
        keyboard_layout.write('Object Further \n') #\b or \n
        #time.sleep(1)
        prox_old = prox

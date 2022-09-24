#This code prints 0 thorugh thee keyboard HID Library when brightness is more than 50% of its highest range
import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import adafruit_apds9960.apds9960
from adafruit_apds9960.apds9960 import APDS9960

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard) 

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
apds = APDS9960(i2c)
apds.enable_color = True

time.sleep(5)
while True:
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    time.sleep(0.005)
    p = (g/65535)
    killSignal = (r/65535)
    print(p)
    if(p>0.5):
          keyboard_layout.write('o')
          time.sleep(0.5)
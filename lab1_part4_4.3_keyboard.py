import time
import analogio
import board
import neopixel
import digitalio
import usb_hid
import adafruit_apds9960.apds9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.color_integration_time=50
sensor.enable_color = True
r, g, b, c = sensor.color_data
a=round(c*255/65535)

while True:
    r, g, b, c = sensor.color_data
    p=round(c*255/65535)
    print(p)
    if p-a<-1:
        keyboard.press(Keycode.BACKSPACE)
    elif p-a>1:
        keyboard.press(Keycode.O)
        keyboard.release_all()
    a=p

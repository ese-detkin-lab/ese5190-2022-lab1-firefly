#brightness control: brightness change synchronously
#gesture control--left--rainbow light show--right--light end. up--uparrow,down--downarrow
import board
import busio
import adafruit_apds9960.apds9960
import neopixel
import time
import analogio
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

i2c = board.STEMMA_I2C()
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
sensor=adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_gesture = True
sensor.enable_color = True
sensor.color_integration_time=50

while True:
    gesture = sensor.gesture()
    r, g, b, c = sensor.color_data
    d=round(c*255*10/65535)
    print(d)
    if gesture==0x03:
        print("left")
        keyboard_layout.write("rainbow light show!^_^\n")
        time.sleep(4)
        pixel.fill((d,0,0))
        time.sleep(1)
        pixel.fill((0,d,0))
        time.sleep(1)
        pixel.fill((0, 0, d))
        time.sleep(1)
        pixel.fill((0, d, d))
        time.sleep(1)
        pixel.fill((d, 0, d))
        time.sleep(1)
        pixel.fill((d, d, 0))
        time.sleep(1)
        pixel.fill((d, d, d))
        time.sleep(1)
    elif gesture == 0x04:
        print("right")
        keyboard_layout.write("The show is end, Thanks>~<!\n")
        pixel.fill((0, 0, 0))
        time.sleep(5)
    elif gesture == 0x01:
        print("up")
        keyboard.press(Keycode.UP_ARROW)
        keyboard.release_all()
        time.sleep(1)
    elif gesture == 0x02:
        print("down")
        keyboard.press(Keycode.DOWN_ARROW)
        keyboard.release_all()
        time.sleep(1)


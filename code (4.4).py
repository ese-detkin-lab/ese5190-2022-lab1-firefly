import time
import board
from adafruit_apds9960.apds9960 import APDS9960
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)
apds.enable_color = True

keys = ["Moving up","Moving down","Moving left","Moving right","\b", Keycode.RETURN,Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.SPACE]
time.sleep(0.1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_color = True
apds.enable_gesture = True


apds.color_integration_time=1


while True:
    r, g, b, c = apds.color_data
    gesture = apds.gesture()
    if gesture == 0x01:
        keyboard_layout.write(keys[0])
        keyboard.press(keys[5])
        keyboard.release_all()
        pixels.fill((c * 30, 0,0))
    elif gesture == 0x02:
        keyboard_layout.write(keys[1])
        keyboard.press(keys[5])
        keyboard.release_all()
        pixels.fill((c * 30, 0, 0))

    elif gesture == 0x03:
        keyboard_layout.write(keys[2])
        keyboard.press(keys[5])
        keyboard.release_all()
        pixels.fill((0, c * 30, 0))

    elif gesture == 0x04:
        keyboard_layout.write(keys[3])
        keyboard.press(keys[5])
        keyboard.release_all()
        pixels.fill((0, c * 30, 0))

    if c>100:
        pixels.fill((0,0, c*30))
        break

    
    








    
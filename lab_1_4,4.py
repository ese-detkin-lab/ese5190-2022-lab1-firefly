import time
import board
from adafruit_apds9960.apds9960 import APDS9960
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keys_pressed = [Keycode.A, Keycode.B,Keycode.C,Keycode.D,Keycode.BACKSPACE]
control_key = Keycode.SHIFT
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

i2c = board.STEMMA_I2C()
i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_color = True
apds.enable_gesture = True


apds.color_integration_time=10
print("waiting to type stuff")

while True:
    r, g, b, c = apds.color_data
    gesture = apds.gesture()
    if gesture == 0x01:
        keyboard.press(control_key,keys_pressed[0])
        keyboard.release_all()
    elif gesture == 0x02:
        keyboard.press(control_key,keys_pressed[1])
        keyboard.release_all()
    elif gesture == 0x03:
        keyboard.press(control_key,keys_pressed[2])
        keyboard.release_all()
    elif gesture == 0x04:
        keyboard.press(control_key,keys_pressed[3])
        keyboard.release_all()
    if r>150:
        keyboard.press(control_key,keys_pressed[4])
        keyboard.release_all()
    if b>150:
        break

#Lab1 4.4
import board
import digitalio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_apds9960.apds9960 import APDS9960

# sensor setup
i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True

# keyboard setup
key_pin_array = []
# The Keycode sent for each button, will be paired with a control key
keys_pressed = [Keycode.A, Keycode.B,Keycode.C,Keycode.BACKSPACE]
control_key = Keycode.SHIFT

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard) 


while True:
    gesture = apds.gesture()

    if gesture == 0x01:
        pass
        print("up")
        key = keys_pressed[0]
        # if isinstance(key, str):
        keyboard.press(control_key, key)  # "Press"...
        keyboard.release_all()  # ..."Release"!
    elif gesture == 0x02:
        pass
        print("down")
        key = keys_pressed[1]
        # if isinstance(key, str):
        keyboard.press(control_key, key)  # "Press"...
        keyboard.release_all()  # ..."Release"!
    elif gesture == 0x03:
        pass
        print("left")
        key = keys_pressed[2]
        #if isinstance(key, str):
        keyboard.press(control_key, key)  # "Press"...
        keyboard.release_all()  # ..."Release"!
    elif gesture == 0x04:
        pass
        print("right")
        key = keys_pressed[3]
        #if isinstance(key, str):
        keyboard.press(control_key, key)  # "Press"...
        keyboard.release_all()  # ..."Release"!
    time.sleep(0.1)
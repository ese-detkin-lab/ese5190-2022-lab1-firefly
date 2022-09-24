# ESE 519 Lab 1     
# Yeqi Chen 
# this is the part 4.4 for ESE 519 Lab 1. By using the gesture sensor of the APDS,
# the program can generate four kinds of keybroad inputs. In order to make it some-what 
# practical in real world, I binded the keys to the WASD, which is the classical control
# keys for FPS games. 
"""CircuitPython Essentials HID Keyboard example"""
import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True
# set up gesture sensor 
apds.ATIME = 0xFF
# The Keycode sent for each button, will be paired with a control key
keys_pressed = [Keycode.W, Keycode.S,Keycode.A,Keycode.D]
control_key = Keycode.SHIFT

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

print("Waiting for key pin...")

while True:
    gesture = apds.gesture()
    #the gesture data
    i = 0
    if gesture == 0x01:
        i = 0 
        print("up")
        #up
    elif gesture == 0x02:
        i = 1        
        print("down")
        #down
    elif gesture == 0x03:
        i = 2
        print("left")
        #left
    elif gesture == 0x04:
        i = 3
        print("right")
        #right

    #print(bool(bright))
    #print ("bright:" + bool(bright) + " dark:"+ bool(dark) + " clear:" + c)
    # Check each pin

    key = keys_pressed[i]  # Get the corresponding Keycode or string
    if isinstance(key, str):  # If it's a string...
        keyboard_layout.write(key)  # ...Print the string
    else:  # If it's not a string...
        keyboard.press(control_key, key)  # "Press"...
        keyboard.release_all()  # ..."Release"!

    time.sleep(1)

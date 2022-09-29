# ESE 5190 LAB1 Firefly part4.4 submission
# Sep 28th 2022, Shu Xu

import busio
import board
import time
import usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# setting up keyboard writing
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# setting up apds9960 sensor
i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_gesture = True
sensor.enable_color = True

# Set ATIME to a smaller value
sensor.color_integration_time = 10

# Setting up control key
control_key = Keycode.BACKSPACE

# The Morse code dictionary
Morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}


# Initialize morse code input
code = ""

time.sleep(0.5)

# Read gesture as morse code:
# Left as dash, Right as dot.
# Up as complete character
# Down as clear/backspace depending on whether there exists any gesture being processed

while True:
    gesture_read = sensor.gesture()
    if gesture_read == 0x01:
        print("up")
        for letter in Morse_dict:
            if Morse_dict[letter] == code:
                keyboard_layout.write(letter)
        code = ""
        #time.sleep(0.2)
    elif gesture_read == 0x02:
        print("down")
        if code == "":
            keyboard.press(control_key)
            keyboard.release_all()
        code = ""
        #time.sleep(0.2)
    elif gesture_read == 0x03:
        print("left")
        code += "-"
        #time.sleep(0.2)
    elif gesture_read == 0x04:
        print("right")
        code += "."
        #time.sleep(0.2)

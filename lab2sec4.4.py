"""Section 4.4 RGB Reader with gesture function
Swipe up: Start detection (1)
Swipe down: Backspace (2)
Swipe left: Undo (Delete new data) (3)
Swipe right : New line ("Enter key") (4)
No Gesture (0)
"""
import time
import analogio
import digitalio
import board
import busio
import adafruit_apds9960.apds9960
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Setup Keyboard
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
# Setup Board
i2c = busio.I2C(board.SCL1, board.SDA1)
apds = adafruit_apds9960.apds9960.APDS9960(i2c)
# Setup Gesture Reading
apds.enable_proximity = True
apds.enable_gesture = True
# Setup Color Detection
apds.enable_color = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
# Change the sampling rate
apds.color_integration_time = 256

# Create key list
key_A = Keycode.A
key_Z = Keycode.Z
command_key = Keycode.COMMAND
control_key = Keycode.CONTROL
shift_key = Keycode.SHIFT
enter_key = Keycode.ENTER
backspace_key = Keycode.BACKSPACE

# Use countdown to set a run time
countdown = 5000
while countdown >= 0:
    countdown = countdown - 1

    gesture = apds.gesture()
    if gesture == 0x01:
        print("Gesture: up")
        r, g, b, c = apds.color_data
        print("Red: {0}, Green: {1}, Blue: {2}, Clear: {3}".format(r, g, b, c))
        keyboard_layout.write("Gesture: Up\n")
        keyboard_layout.write(
            "Red: {0}, Green: {1}, Blue: {2}, Clear: {3}\n".format(r, g, b, c)
        )
        keyboard.release_all()
    elif gesture == 0x02:
        print("Gesture: down")
        keyboard_layout.write("Gesture: Down\n")
        keyboard.press(backspace_key)
        keyboard.release_all()
    elif gesture == 0x03:
        print("Gesture: left")
        keyboard_layout.write("Gesture: Left\n")
        keyboard.press(command_key, key_Z)  # Only on iOS
        keyboard.release_all()
    elif gesture == 0x04:
        print("Gesture: right")
        keyboard_layout.write("Gesture: Right\n")
        keyboard.press(enter_key)
        keyboard.release_all()

    time.sleep(0.01)

print("Time's up. Reload program.")

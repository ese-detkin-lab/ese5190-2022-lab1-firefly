import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import busio
import adafruit_apds9960.apds9960

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

# Enable Color detection
sensor.enable_color = True

# Enable Proximity detection
sensor.enable_proximity = True

# Enable Gesture Sensing
sensor.enable_gesture = True

# Tweak the `color_integration_time` property.
sensor.color_integration_time = 50

# The Keycode sent for each button, will be paired with a control key
control_key = Keycode.BACKSPACE

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

while True:
    # Get the color data from the sensor.
    r, g, b, c = sensor.color_data

    # Convert the sensor value from `65536` to `255`.
    c_255 = (c/65536) * 255

    # Print the Current Brightness Value
    print("Brightness Value : " ,c_255)
    
    if c_255 >=0 and c_255 < 100: # If the brightness value is less than 100
        keyboard_layout.write("This is very Dim!!\n")  # ...Print the string
    elif c_255 >= 100 and c_255 < 190: # If the Brighness value > 100 and < 190
        keyboard.send(control_key) # Send the backspace key.
    else:  # If it's not a string...
        keyboard.press(control_key)  # "Press"...
        keyboard.release_all() # ..."Release"!
    
    # Check for any gestures.
    gesture_num = sensor.gesture()

    # If the gesture is a right or a left, break from
    # the while loop.
    if gesture_num == 4 or gesture_num == 3:
        break
    
    # Sleep for 0.05 seconds, for smooth performance.
    time.sleep(0.05)

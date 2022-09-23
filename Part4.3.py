import time
import board
import digitalio
import usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
print("This is Tippy's 4.3")


if __name__ =="__main__":
    i2c = board.STEMMA_I2C()
    apds = APDS9960(i2c)
    apds.color_integration_time=16
    # apds.enable_proximity = True
    # apds.enable_gesture
    apds.enable_color=True
    bright=0
    bright_prev=0
    tolerance = 100

    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the
    # led.direction = digitalio.Direction.OUTPUT

    print("Waiting for key pin...")

    while True:
        _,_,_,bright=apds.color_data
        if bright>bright_prev+tolerance:
            keyboard_layout.write("o")
        elif bright<bright_prev-tolerance:
            keyboard.send(Keycode.BACKSPACE)
        else :
            continue
        bright_prev=bright
        print(bright)
        time.sleep(0.1)

import time
import board
import digitalio
import usb_hid
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
print("This is Tippy's 4.4")
pixels = neopixel.NeoPixel(board.NEOPIXEL,1)
if __name__ =="__main__":
    i2c = board.STEMMA_I2C()
    apds = APDS9960(i2c)
    apds.color_integration_time=100

    apds.enable_color=True
    apds.enable_gesture = True
    bright=0
    bright_prev=0
    tolerance = 200
    str1 = "Object Going up\n"
    str2 = "Object Going down\n"
    str3 = "Object turns left\n"
    str4 = "Object turns right\n"
    key_pressed = ["Hi,Tippy's world\n Game for change the light\n","Open the flashlight","Close the flashlight","\tGood Closer\n","\tGood Further\n","Hhh Have fun\n"]
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the
    # led.direction = digitalio.Direction.OUTPUT
    # define mouse
    mouse = Mouse(usb_hid.devices)
    print("Waiting for key pin...")
    key = key_pressed[0]
    keyboard_layout.write(key)
    time.sleep(2)
    key = key_pressed[1]
    keyboard_layout.write(key)
    time.sleep(2)
    i = 8
    r = 0
    while i:
        r,g,b,bright=apds.color_data
        gesture = apds.gesture()
        if gesture == 1:
            mouse.move(y = 80)
            keyboard_layout.write(str1)
        if gesture == 2:
            mouse.move(y = -80)
            keyboard_layout.write(str2)
        if gesture == 3:
            mouse.move(x = 80)
            keyboard_layout.write(str3)
        if gesture == 4:
            mose.move(x = -80)
            keyboard_layout.write(str4)
        if bright > bright_prev + tolerance and i % 2 == 0:
            pixels.fill((0,255,0))
            i = i - 1
            key = key_pressed[3]
            keyboard_layout.write(key)
            key = key_pressed[2]
            keyboard_layout.write(key)
            time.sleep(2)
        if bright<bright_prev-tolerance and i % 2 == 1:
            pixels.fill((0,0,255))
            i = i - 1
            key = key_pressed[4]
            keyboard_layout.write(key)
            time.sleep(1)
            if i != 0:
                key = key_pressed[1]
                keyboard_layout.write(key)
        print(print('{0},\t{1}'.format(bright, bright_prev)))
        bright_prev=bright
        pixels.fill((0,0,0))

    time.sleep(2)
    pixels.fill((255,255,255))
    key = key_pressed[5]
    keyboard_layout.write(key)
    time.sleep(1)
    keyboard_layout.write("\nKeyboard abort")
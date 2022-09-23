import time
import analogio
import board
import digitalio
import usb_hid
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)


while True:
     # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the data and print the different channels
    r, g, b, c = apds.color_data
    print("red: ", r)
    print("green: ", g)
    print("blue: ", b)


    a = [r,g,b]
    x=max(a)

    time.sleep(0.1)
    #decide color
    if r == x :
         keyboard.press(Keycode.R)
         keyboard.release_all()
         keyboard.press(Keycode.E)
         keyboard.release_all()
         keyboard.press(Keycode.D)
         keyboard.release_all()

    if g == x:
         keyboard.press(Keycode.G)
         keyboard.release_all()
         keyboard.press(Keycode.R)
         keyboard.release_all()
         keyboard.press(Keycode.E)
         keyboard.release_all()
         keyboard.press(Keycode.E)
         keyboard.release_all()
         keyboard.press(Keycode.N)
         keyboard.release_all()

    if b == x:
         keyboard.press(Keycode.B)
         keyboard.release_all()
         keyboard.press(Keycode.L)
         keyboard.release_all()
         keyboard.press(Keycode.U)
         keyboard.release_all()
         keyboard.press(Keycode.E)
         keyboard.release_all()
# 在这里写上你的代码 :-)

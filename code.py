import time
import board
import usb_hid
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
mouse=Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

apds.enable_color = True
apds.enable_gesture=True

apds.color_integration_time=0x22

current_lux=0
enter_key = Keycode.ENTER
backspace_key=Keycode.BACKSPACE

str_1="Be careful! It getting dark!"
str_2="All safe, brighter now."
str_3="An object just climbed up!"
str_4="An object just fell down!"
str_5="An object just turned left!"
str_6="An object just turned right!"


time.sleep(6)
while True:
    
    r, g, b, c = apds.color_data
    lux=colorutility.calculate_lux(r,g,b)
    pixels.fill((r, g, b))
    
    if current_lux>lux*1.5:
        keyboard_layout.write(str_1)
        time.sleep(0.4)
        for i in range(len(str_1)):
            keyboard.press(backspace_key)
            keyboard.release_all()
        current_lux=lux
    elif current_lux<lux/1.5:
        keyboard_layout.write(str_2)
        time.sleep(0.4)
        for i in range(len(str_2)):
            keyboard.press(backspace_key)
            keyboard.release_all()
        current_lux=lux


    gesture = apds.gesture()

    if gesture == 1:
        keyboard_layout.write(str_3)
        mouse.move(wheel=-20)
        time.sleep(0.4)
        mouse.move(wheel=20)
        for i in range(len(str_3)):
            keyboard.press(backspace_key)
            keyboard.release_all()

    if gesture == 2:
        keyboard_layout.write(str_4)
        mouse.move(wheel=20)
        time.sleep(0.4)
        mouse.move(wheel=-20)
        for i in range(len(str_4)):
            keyboard.press(backspace_key)
            keyboard.release_all()

    if gesture == 3:
        keyboard_layout.write(str_5)
        time.sleep(0.4)
        for i in range(len(str_5)):
            keyboard.press(backspace_key)
            keyboard.release_all()

    if gesture == 4:
        keyboard_layout.write(str_6)
        time.sleep(0.4)
        for i in range(len(str_6)):
            keyboard.press(backspace_key)
            keyboard.release_all()

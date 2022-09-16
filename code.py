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
apds.enable_proximity = True

apds.color_integration_time=0x22

current_lux=0
enter_key = Keycode.ENTER
backspace_key=Keycode.BACKSPACE
crtl_key=Keycode.CONTROL
a_key=Keycode.A

str_1="Be careful! It getting dark!\n"
str_2="All safe, brighter now.\n"
str_3="An object just climbed up!\n"
str_4="An object just fell down!\n"
str_5="An object just turned left!\n"
str_6="An object just turned right!\n"


time.sleep(6)
while True:
    
    strs=""
    r, g, b, c = apds.color_data
    lux=colorutility.calculate_lux(r,g,b)
    pixels.fill((r, g, b))

    if current_lux>lux*1.5:
        strs+=str_1
        current_lux=lux
    elif current_lux<lux/1.5:
        strs+=str_2
        current_lux=lux


    gesture = apds.gesture()

    if gesture == 1:
        strs+=str_3

    if gesture == 2:
        strs+=str_4

    if gesture == 3:
        strs+=str_5

    if gesture == 4:
        strs+=str_6

    keyboard_layout.write(strs)
    time.sleep(1)
    for i in range(len(strs)):
        # print(len(strs))
        keyboard.press(backspace_key)
        keyboard.release_all()



    

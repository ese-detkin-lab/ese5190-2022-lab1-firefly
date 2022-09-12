import time
import board
import digitalio
import analogio
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
apds.enable_proximity=True
apds.enable_gesture=True

apds.color_integration_time=0x22
def color(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

current_lux=0
control_key = Keycode.ENTER

while True:
    # while not apds.color_data_ready:
    #     time.sleep(0.005)
    
    r, g, b, c = apds.color_data
    lux=colorutility.calculate_lux(r,g,b)
    pixels.fill((r, g, b))
    if current_lux>lux*1.5:
        keyboard_layout.write('Be careful! It getting dark!')
        keyboard.press(control_key)
        keyboard.release_all()
        current_lux=lux
    elif current_lux<lux/1.5:
        keyboard_layout.write('All safe, brighter now.')
        keyboard.press(control_key)
        keyboard.release_all()
        current_lux=lux


    gesture = apds.gesture()
    if gesture == 1:
        keyboard_layout.write('An object just climbed up!')
        keyboard.press(control_key)
        keyboard.release_all()
    if gesture == 2:
        keyboard_layout.write('An object just fell down!')
        keyboard.press(control_key)
        keyboard.release_all()
    if gesture == 3:
        keyboard_layout.write('An object just turned left!')
        keyboard.press(control_key)
        keyboard.release_all()
    if gesture == 4:
        keyboard_layout.write('An object just turned right!')
        keyboard.press(control_key)
        keyboard.release_all()
    



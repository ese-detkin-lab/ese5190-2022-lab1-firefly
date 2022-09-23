import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
from adafruit_hid.mouse import Mouse
import usb_hid
import neopixel
# Keyboard
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
mouse = Mouse(usb_hid.devices)

# Keyboard setting
time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
apds.enable_proximity = True
apds.color_integration_time = 100

clear = 0;
proxy = 0;

keys_shown = ["Colder!\n", "Warmer!\n", "Sweet!\n"]

while True:
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the data and print the different channels
    r, g, b, c = apds.color_data
    print("red: ", r)
    print("green: ", g)
    print("blue: ", b)
    print("clear: ", c)

    pixels.fill((c*255/10000, c*255/10000, c*255/10000))

    print("color temp {}".format(colorutility.calculate_color_temperature(r, g, b)))
    print("light lux {}".format(colorutility.calculate_lux(r, g, b)))

    mouse.move(x=int((c - clear)/20))

    #if c - clear > 200 :
    #    keyboard.press(Keycode.O)
    #    keyboard.release_all()

    #if clear - c > 200:
    #    keyboard.press(Keycode.BACKSPACE)
    #    keyboard.release_all()

    clear = c

    proxy_measured = apds.proximity

    if proxy_measured > 180 :
        if(proxy_measured - proxy > 0) :
            keyboard_layout.write(keys_shown[0]) #colder
            #keyboard.release_all()
        else :
            keyboard_layout.write(keys_shown[1])
            #keyboard.release_all()
    elif proxy_measured == 0 :
        time.sleep(0.001)
    elif proxy_measured < 120 :
        if(proxy_measured - proxy > 0) :
            keyboard_layout.write(keys_shown[1]) #warmer
            #keyboard.release_all()
        else :
            keyboard_layout.write(keys_shown[0])
            #keyboard.release_all()
    else:
        keyboard_layout.write(keys_shown[2])


    proxy = proxy_measured

    time.sleep(0.5)

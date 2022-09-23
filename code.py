import board
import busio
import time
import adafruit_apds9960.apds9960
import neopixel

import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

#i2c = board.STEMMA_I2C()
i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_color = True
sensor.enable_gesture = True
sensor.color_integration_time = 10               # Q.2.3

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

mouse = Mouse(usb_hid.devices)

keys_pressed = [Keycode.O, Keycode.BACKSPACE]
control_key = Keycode.SHIFT
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Q.2.1
'''
while True:
    print(sensor.proximity)
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
'''
# Q.2.2
'''
while gesture == 0OO
    gesture = sensor.gesture()
    print('Saw gesture: {0}'.format(gesture))
'''
#Q.3.1-Q.3.2
'''
c_last = 0                                             # initialize the parameter
while True:
    r, g, b, c = sensor.color_data                     # track the reading from color sensor
    print(c)
    if c >= (c_last+100):                              # indicate that it is going bright
        pixels.fill((255, 255, 255))                   # RP2040's LED display (on)
    elif c <= (c_last-100):                            # indicate that is going dim
        pixels.fill((0, 0, 0))                         # RP2040's LED display (off)
    c_last = c
'''

#Q.4.1/4.2
'''
c_last = 0
while True:
    r, g, b, c = sensor.color_data
    print(c)
    if c >= (c_last+100):
        mouse.move(x=20)
        key = key_pressed[0]
        keyboard.press(control_key, key)
        keyboard.release_all()

    elif c <= (c_last-100):
        mouse.move(x=-20)
        key = key_pressed[1]
        keyboard.press(control_key, key)
        keyboard.release_all()
    c_last = c
    #time.sleep(0.1)
'''

# Q.4.4
c_last = 0
while True:
    time.sleep(2)
    info = keyboard_layout.write("Test gesture first!\n")
    i = 0
    while i <= 3:
        gesture = sensor.gesture()

        if gesture == 1:
            info = keyboard_layout.write("Going up!\n")
            time.sleep(0.1)
            i += 1
        if gesture == 2:
            info = keyboard_layout.write("Going down!\n")
            time.sleep(0.1)
            i += 1
        if gesture == 3:
            info = keyboard_layout.write("Going left!\n")
            time.sleep(0.1)
            i += 1
        if gesture == 4:
            info = keyboard_layout.write("Going right!\n")
            time.sleep(0.1)
            i += 1
    time.sleep(1)
    info = keyboard_layout.write("Then test brightness!\n")
    i = 0
    while i <= 3:
        r, g, b, c = sensor.color_data
        if c >= (c_last+100):
            info = keyboard_layout.write("Going bright!\n")
            time.sleep(0.5)
            i += 1
        elif c <= (c_last-100):
            info = keyboard_layout.write("Going dark!\n")
            time.sleep(0.5)
            i += 1
        c_last = c
    info =keyboard_layout.write("Done\n")
    break




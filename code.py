import usb_hid
import time
import board
import busio
import adafruit_apds9960.apds9960
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.color_integration_time=150
sensor.enable_proximity = True
sensor.enable_color = True
sensor.enable_gesture = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
r, g, b, c = sensor.color_data
c1=c
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
flag = 0
time.sleep(5)  #use for reserving the time for me to open txt

while(1):
    gesture = sensor.gesture()
    r, g, b, c = sensor.color_data
    if(c<20000 and c>500):
        if(flag==1):
            kbd.press(Keycode.BACKSPACE)
            kbd.release(Keycode.BACKSPACE)
            layout.write('o')
            flag=0
        if gesture == 0x01:        #up
            kbd.press(Keycode.BACKSPACE)
            kbd.release(Keycode.BACKSPACE)
            kbd.press(Keycode.UP_ARROW)
            kbd.release(Keycode.UP_ARROW)
            layout.write('o')
            print("up")
        elif gesture == 0x02:       #down
            kbd.press(Keycode.BACKSPACE)
            kbd.release(Keycode.BACKSPACE)
            kbd.press(Keycode.DOWN_ARROW)
            kbd.release(Keycode.DOWN_ARROW)
            layout.write('o')
            print("down")
        elif gesture == 0x03:       #left
            kbd.press(Keycode.BACKSPACE)
            kbd.release(Keycode.BACKSPACE)
            kbd.press(Keycode.LEFT_ARROW)
            kbd.release(Keycode.LEFT_ARROW)
            layout.write('o')
            print("left")
        elif gesture == 0x04:       #right
            kbd.press(Keycode.BACKSPACE)
            kbd.release(Keycode.BACKSPACE)
            kbd.press(Keycode.RIGHT_ARROW)
            kbd.release(Keycode.RIGHT_ARROW)
            layout.write('o')
            print("right")

    elif(c>=20000):
        if(flag==0):
            kbd.press(Keycode.BACKSPACE)
            kbd.release(Keycode.BACKSPACE)
            layout.write('X')
            flag=1
            
    else:
        break






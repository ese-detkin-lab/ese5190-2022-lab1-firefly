import usb_hid
import time
import board
import busio
import adafruit_apds9960.apds9960
import neopixel
import random
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
#configuration
i2c = board.I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.color_integration_time=10
sensor.enable_proximity = True
sensor.enable_color = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
key = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(key)
#read data
gesture = sensor.gesture()
distance_last=sensor.proximity
r, g, b, c_last = sensor.color_data
#delay for keyboard file open
print("Keyboard start writing! Prerpare your txt and hands!\n")
time.sleep(5)
i=5
score=0
while(i):
    layout.write('New Round:\n')
    distance=sensor.proximity
    time.sleep(0.1)
    if(distance>200) and (distance<5):
       number=-number
    else:
       number=random.uniform(-1,1)

    if(number<=0):
       layout.write('Get your hand closely! \n')
       time.sleep(2)
       r, g, b, c_new = sensor.color_data
       if((c_new<c_last+20)):
            pixels.fill((255, 255, 255))
            layout.write('You are right\n ')
            score=score+1
       elif((c_new>=c_last+20)):
            layout.write('You are wrong\n')
            pixels.fill((255, 0, 0))
            score=score-1
    elif(number>0):
       layout.write('Get your hand further!\n ')
       time.sleep(2)
       r, g, b, c_new = sensor.color_data
       if((c_new<=c_last+20)):
            pixels.fill((255, 0, 0))
            layout.write('You are wrong\n')
            score=score-1
       elif((c_new>c_last+20)):
            layout.write('You are right\n')
            pixels.fill((255, 255, 255))
            score=score+1
    else:
        key.press(Keycode.BACKSPACE)
        key.release(Keycode.BACKSPACE)
    time.sleep(1)
    c_last=c_new
    time.sleep(2)
    i=i-1
layout.write('GAME OVER')
print('Your score point is:')
print(score)

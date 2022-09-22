import board
import time
from adafruit_apds9960.apds9960 import APDS9960
import neopixel

i2c = board.I2C()
sensor = APDS9960(i2c)
sensor.enable_gesture = True
sensor.enable_color = True
sensor.enable_proximity = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
sensor.color_integration_time=100


while True:
    gesture = sensor.gesture()
    distance=sensor.proximity
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    if c>1040 :
       
    elif c<1040:
       pixels.fill((0, 0, 0))

'''
    if gesture == 0x01:
        print("up")
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:
        print("left")
    elif gesture == 0x04:
        print("right")
        print("right")


import busio
import time
import board
from adafruit_apds9960.apds9960 import APDS9960

i2c = busio.I2C(board.SCL1, board.SDA1)
apds = APDS9960(i2c)

apds.enable_proximity = True
apds.enable_color = True
apds.enable_gesture = True

while True:
    print('Proximity:')
    print(apds.proximity)
    r, g, b, c = apds.color_data
    print('Colour data:')
    print('\tRed: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    gesture = apds.gesture()
    while gesture == 0:
        gesture = apds.gesture()
    print('Gesture:')
    print(gesture)
    time.sleep(0.2)
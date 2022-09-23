# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Mouse example"""
import time
#import analogio
import board
#import digitalio
import adafruit_apds9960.apds9960
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_color = True
'''
x_axis = analogio.AnalogIn(board.A0)
y_axis = analogio.AnalogIn(board.A1)
select = digitalio.DigitalInOut(board.A2)
select.direction = digitalio.Direction.INPUT
select.pull = digitalio.Pull.UP
'''
pot_min = 0.00
pot_max = 3.29
step = (pot_max - pot_min) / 20.0


def get_brightness():
    sensor.color_integration_time = 1 #the maxinum value of c is 1025
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    return c

'''
def steps(axis):
    """ Maps the potentiometer voltage range to 0-20 """
    return round((axis - pot_min) / step)
'''

while True:
    x = get_brightness( )
    #y = get_voltage(y_axis)

    #if select.value is False:
        #mouse.click(Mouse.LEFT_BUTTON)
        #time.sleep(0.2)  # Debounce delay

    if x > 400.0:
        # print(steps(x))
        mouse.move(x=1)
    if x < 400.0:
        # print(steps(x))
        mouse.move(x=-1)
'''
    if steps(x) > 19.0:
        # print(steps(x))
        mouse.move(x=8)
    if steps(x) < 1.0:
        # print(steps(x))
        mouse.move(x=-8)

    if steps(y) > 11.0:
        # print(steps(y))
        mouse.move(y=-1)
    if steps(y) < 9.0:
        # print(steps(y))
        mouse.move(y=1)

    if steps(y) > 19.0:
        # print(steps(y))
        mouse.move(y=-8)
    if steps(y) < 1.0:
        # print(steps(y))
        mouse.move(y=8)
'''
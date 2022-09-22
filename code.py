#######################################
# Nikola Obradovic
# 2022-09-10
# ESE 5190
# Lab 1
#######################################

import time
import math

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

import busio
import adafruit_apds9960.apds9960

def clamp_value(value, minval, maxval):
    if value < minval:
        value = minval
    elif value > maxval:
        value = maxval
    return value

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard) 

i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_color = True
sensor.color_integration_time = 10
time.sleep(0.8)


r, g, b, c = sensor.color_data

indicator = 0       #percentage to which the bar should be filled
max_indicator = 100 #maximum number of characters that should be used to fill the bar
beta = 0.5          #smoothing coefficient
max_count = 200     #max reasonable sensor reading from this spot on my couch (kitchen lights on)
min_count = 10      #min reasonable sensor reading from this spot on my couch (kitchen lights on)

smoothed_value = c

#Wait for user to start program by shining a bright light
print("Waiting for brightness...")

while c < 8000:
    r, g, b, c = sensor.color_data
    smoothed_value = (smoothed_value*beta) + (clamp_value(c, min_count, max_count)*(1-beta))

print("Starting program...")
#Run the program until the user cancels by covering the sensor
while c > 5:
    r, g, b, c = sensor.color_data
    clamped_value = clamp_value(c, min_count, max_count)

    #filter the reading to reduce the jitter
    smoothed_value = (smoothed_value*beta) + (clamped_value*(1-beta))


    newindicator = int((smoothed_value/max_count) * max_indicator)
    indicatordelta = int(newindicator - indicator)  
    #Print some debug info to the console
    out_txt = "{c_o:.3f}\t{smoothed_value_o:.3f}\t{newind_o:.3f}\t{delta_o:.3f}\t{indicator_o:.3f}"
    print(out_txt.format(c_o = c, smoothed_value_o = smoothed_value, newind_o = newindicator, delta_o = indicatordelta, indicator_o = indicator))
    
    if indicatordelta > 0:
        for i in range(abs(indicatordelta)):
            keyboard.press(Keycode.BACKSLASH)
            keyboard.release_all()
            pass
    elif indicatordelta < 0:
        for i in range(abs(indicatordelta)):
            keyboard.press(Keycode.BACKSPACE)
            keyboard.release_all()
            pass
    else:
        pass
    indicator = newindicator
    time.sleep(0.1)
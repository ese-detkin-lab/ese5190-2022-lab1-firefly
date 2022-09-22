import board
import busio
import neopixel
import adafruit_apds9960.apds9960
from time import sleep
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

#initialization of Sensor Board APDS9960
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)#Initializing the I2C port for Qwwic Connector

#mode Enable
sensor.color_integration_time = 255 #ADC Intergration time/Number of Cycles/Count   color_integration_time:time(255:2.78ms,219:103ms)
sensor.enable_color = True #Enable Color Sensor

#CircuitPy HID Keyboard Initialization
sleep(1)  # Sleep for a bit to avoid a race condition on some systems
mouse = Mouse(usb_hid.devices)

bar_previous = 0
while True:
    r, g, b, c = sensor.color_data
    if c >= 50: To avoid the mouse to go Crazy, before starting the code the sensor needs to be covered
        r, g, b, c = sensor.color_data
        bar = int(c*1000/65535) #Converting to a scale of 1000
        if bar-bar_previous > 0:  #If brightness increases, move mouse to the right by 1
            for i in range(abs(bar-bar_previous)):
                mouse.move(x=1)
        elif bar - bar_previous < 0: #If brightness increases, move mouse to the left by 1
            for i in range(abs(bar-bar_previous)):
                mouse.move(x=-1)
        bar_previous = bar






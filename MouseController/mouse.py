import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

#Neopixel LED and Sensor Initialization
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.I2C()
apds = APDS9960(i2c)
apds.enable_color = True
apds.color_integration_time=1
apds.color_gain=3

mouse = Mouse(usb_hid.devices)
#Define axes of mouse
x_axis = analogio.AnalogIn(board.A0)
y_axis = analogio.AnalogIn(board.A1)
select = digitalio.DigitalInOut(board.A2)
select.direction = digitalio.Direction.INPUT

select.pull = digitalio.Pull.UP

#Define step movement of mouse
pot_min = 0.00
pot_max = 3.29
step = (pot_max - pot_min) / 20.0

def steps(axis):
    """ Maps the potentiometer voltage range to 0-20 """
    return round((axis - pot_min) / step)
    
while True:
    while not apds.color_data_ready:
        time.sleep(0.5)
    r, g, b, c = apds.color_data
    print("light lux {}".format(colorutility.calculate_lux(r, g, b)))
    #Color intensity dependent Neopixel dimming
    lux_value= colorutility.calculate_lux(r,g,b)
    rgb=int(lux_value/4)
    #Move right if bright
    if steps(rgb) > 0:
        mouse.move(x=2)
    #Move left if dark
    if steps(rgb) == 0:
        mouse.move(x=-2)

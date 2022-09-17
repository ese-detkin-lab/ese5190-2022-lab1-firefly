# Manipulate the keyboard. 
# Type 'o' when brightness increases, and send a 'backspace' command when the brightness decreases.
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
import board
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
kbd = Keyboard(usb_hid.devices)



prev = 0
while True:
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)
        
    # get the data and print the different channels
    r, g, b, c = apds.color_data
    
    if (r + g + b)/ 65535 > prev:
        kbd.send(Keycode.O)
    else:
        kbd.send(Keycode.BACKSPACE)
    
    
    prev = ((r + g + b)/65535)


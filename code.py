# add necessary imports
import busio
import adafruit_apds9960.apds9960
import time
import neopixel
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# initialize the board and sensors and neopixel libraries
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

# initialize keyboard
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# enable sensing color for ADPDS9960
sensor.enable_color = True

# initialize quote to whatever string
# I chose one of my favorite quotes from Game of Thrones
quotes = "Never forget what you are. The rest of the world will not. Wear it like armor, and it can never be used to hurt you."
# initialize a variable that will keep track of string positon
i = 0

# wait for 5 seconds before starting to ensure enough time to switch to Word / Notes file.
time.sleep(5)

# enable while loop so that it ends after the entire string has been printed
while i < len(quotes):
    
    # grab color data from sensor
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    
    # map the brightness channel of the sensor data to a value between 0 and 1
    brightness_level = (c / 65536) * 1
    
    # if the brightness level is greater than 0.5
    # set LED on RP2040 to Green
    # start printing the next letter in the quote
    # increment i by 1
    if brightness_level > 0.5:
        pixels.fill((0, 255, 0))
        keyboard_layout.write(quotes[i])
        i += 1
        
    # otherwise fill LED on RP2040 to Red
    # start deleting letters from the quote
    # keep track of updated position by subtracting 1 from i
    # ensure that i never goes below zero by adding a conditional
    else:
        pixels.fill((255, 0, 0))
        keyboard.press(Keycode.BACKSPACE)
        keyboard.release_all()
        i -= 1
        if i < 0:
            i = 0
            
    # pause for 0.1 seconds for system to catch up
    time.sleep(0.1)


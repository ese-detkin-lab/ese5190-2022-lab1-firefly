import time
import board
import usb_hid
from adafruit_hid.mouse import Mouse
import busio
import adafruit_apds9960.apds9960

mouse = Mouse(usb_hid.devices)

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

# Enable Color detection
sensor.enable_color = True

# Enable Proximity detection
sensor.enable_proximity = True

# Tweak the `color_integration_time` property.
sensor.color_integration_time = 50


while True:
    # Get the color data from the sensor.
    r, g, b, c = sensor.color_data

    # Convert the sensor value from `65536` to `255`.
    c_255 = (c/65536) * 255

    # Print the Current Brightness Value
    print("Brighness Value : " ,c_255)

    # Move the mouse cursor, based on the value in `c_255`.
    if c_255 >= 0 and c_255 < 50:
        mouse.move(x=1)
    elif c_255 >= 50 and c_255 < 100:
        mouse.move(x=-2)
    elif c_255 >= 100 and c_255 < 150:
        mouse.move(x=3)
    elif c_255 >= 150 and c_255 < 200:
        mouse.move(x=-4)
    else:
        mouse.move(x=5)

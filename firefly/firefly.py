import board
import busio
import adafruit_apds9960.apds9960
import time
import neopixel

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

# Enable Color detection
sensor.enable_color = True

# Enable Proximity detection
sensor.enable_proximity = True

# Tweak the `color_integration_time` property.
sensor.color_integration_time = 50

# Initialize the LED, on the RP2040
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

# Run an infinite loop.
while True:
    # Get the color data from the sensor.
    r, g, b, c = sensor.color_data

    # Convert the sensor value from `65536` to `255`.
    c_255 = (c/65536) * 255

    # Pass, the value obtained above, to the LED, in the `Blue` Channel.
    pixels.fill((0, 0, c_255))

    # Wait for some time, for smooth operation.
    time.sleep(0.0003)

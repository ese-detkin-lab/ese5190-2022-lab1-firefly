import board
import busio
import time
import adafruit_apds9960.apds9960
import neopixel

# setting up apds9960 sensor
i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

# enable APDS9960 color sensor
sensor.enable_color = True

# Set ATIME to a smaller value
sensor.color_integration_time = 10

# setting up on-board LED
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    # Color reading
    r, g, b, c = sensor.color_data
    # print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))

    # Determine if the object is bright
    if c > 200:
        pixels.fill((255, 0, 0))
    else:
        pixels.fill((0, 0, 0))

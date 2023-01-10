import board
import busio
import adafruit_apds9960.apds9960
import time
import neopixel
i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_color = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
sensor.color_integration_time = 10
clast = 0
while True:
    r, g, b, c = sensor.color_data
    print(c)
    if(c > clast+5):
        pixels.fill((255,0,0))
    else:
        pixels.fill((0,0,0))
    clast = c
    time.sleep(0.05)


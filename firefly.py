import board
import neopixel
import busio
import adafruit_apds9960.apds9960
import time

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_color = True
gesture = sensor.gesture()

sensor.color_integration_time = 10



while True:
    r, g, b, c = sensor.color_data
    print("r: {}, g: {}, b: {}, c: {}".format(r, g, b, c))
    if c >= 80:
        led.fill((255, 255, 0)) # turn on the led on the board
    else:
        led.fill((0, 0, 0))
    
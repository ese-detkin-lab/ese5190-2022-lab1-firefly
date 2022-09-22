import time
import board
import busio
import adafruit_apds9960.apds9960
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.color_integration_time = 10

sensor.enable_proximity = True
sensor.enable_color = True

while True:
    while not sensor.color_data_ready:
        time.sleep(0.005)

    r, g, b, c = sensor.color_data
    print("r: {}, g: {}, b: {}, c: {}".format(r, g, b, c))

    pixels.fill((c/16, c/16, c/16))


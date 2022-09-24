import board
import time
import neopixel
import busio
import adafruit_apds9960.apds9960

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_color = True

time.sleep(2)
while True:
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    flag = (c/65535)*255
    pixels.fill((flag,0,0))






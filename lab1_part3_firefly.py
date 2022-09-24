import board
import busio
import adafruit_apds9960.apds9960
import neopixel
import time

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.color_integration_time=20
sensor.enable_color = True

while True:
    r, g, b, c = sensor.color_data
    #print('Clear: {3}'.format(r, g, b, c))
    d=c*255*10/65535
    print(d)
    pixel.fill((d, d, 0))

import board
import busio
import adafruit_apds9960.apds9960
import neopixel
import time
led = neopixel.NeoPixel(board.NEOPIXEL,1)
i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.color_integration_time=1
sensor.enable_color = True

while True:
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    
    led.fill((c,c,c))
    
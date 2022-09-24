import time
import analogio
import board
import neopixel
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
import adafruit_apds9960.apds9960

mouse = Mouse(usb_hid.devices)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.color_integration_time=50
sensor.enable_color = True
r, g, b, c = sensor.color_data
a=round(c*255/65535)

while True:
    r, g, b, c = sensor.color_data
    #print('Clear: {3}'.format(r, g, b, c))
    p=round(c*255/65535)
    print(p)
    if p-a<-1:
        mouse.move(x=-10)
    elif p-a>1:
        mouse.move(x=10)
    a=p

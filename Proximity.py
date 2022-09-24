import board
import adafruit_apds9960.apds9960
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
while True:
    print(sensor.proximity)


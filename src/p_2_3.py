import board
import busio
import adafruit_apds9960.apds9960
i2c = busio.I2C(board.SCL1, board.SDA1) # set up sensor i2c comms on the STEMMA connector pins
apds = adafruit_apds9960.apds9960.APDS9960(i2c) # adafruit_apds9960.apds9960.APDS9960() constructs a new object "instance" for interacting with the sensor
print(apds.color_integration_time) # check/set property on the instance, not the constructor
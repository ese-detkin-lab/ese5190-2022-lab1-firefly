"""Get Proximity, Colors and Gesture"""
import board
import busio
import adafruit_apds9960.apds9960

#i2c = busio.I2C(board.SCL1, board.SDA1) #either i2c setting works
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

#Umcomment to run each section
"""
#Proximity
sensor.enable_proximity = True
while True:
    print(sensor.proximity)
"""

"""
#Coloring
sensor.enable_color = True
#Change the sampling time
sensor.color_integration_time = 50
while True:
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
"""
   
#Gesture Reading
sensor.enable_proximity = True
sensor.enable_gesture = True
gesture = sensor.gesture()
while gesture == 0:
    gesture = sensor.gesture()
print('Saw gesture: {0}'.format(gesture))

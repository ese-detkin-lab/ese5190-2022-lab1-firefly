#libraries Needed for the Project
import board
import busio
import neopixel #on Board LED Control
import adafruit_apds9960.apds9960 #Sensor Board Control
from time import sleep

#initialization of Sensor Board APDS9960
i2c = board.STEMMA_I2C() #Initializing the I2C port for Qwwic Connector
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

#mode Enable
sensor.color_integration_time = 255 #ADC Intergration time/Number of Cycles/Count   color_integration_time:time(255:2.78ms,219:103ms)
sensor.enable_color = True #Enable Color Sensor

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1) #Enable LED

Moving_Average_List=[]

r, g, b, c = sensor.color_data
for i in range(200):
    mal.append(c)  #Storing 200 samples of sensor for average calculation

while True:
    r, g, b, c = sensor.color_data
    Moving_Average_List.pop(0) #Deleting first sample from the list
    Moving_Average_List.append(c) #Adding new sample to the list

    if c > sum(mal)/200:  #Calculating the moving average and using it as a threshold for LED Blinking
        pixels.fill((c, c, 0))
    else:
        pixels.fill((0, 0, 0))

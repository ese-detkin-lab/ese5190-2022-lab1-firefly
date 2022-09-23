University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Zhijing Yao
        Facebook: ZhijingYao
    Tested on: MacBook Pro (13-inch, 2018), macOS Big Sur 11.2.3
    
    
The primary idea of my 4.4 design mainly utilized the proximity property of the sensor. In my code, I set the space that is 120-180 away from the sensor as a "sweet" space. The user can approach the APDS9960 sensor with their finger. If the finger is above the "sweet" height and is getting closer to it, the RP2040 will print "Warmer" on the PC. If the finger is above the "sweet" height but moving away from it, the RP2040 will print "Colder" to tell the user to come back. Vice versa. If the finger is at a position below the "sweet" height and moving towards it, the RP2040 will print "Warmer". And if it's moving away from the "sweet" height, "Colder" will be printed. If the sensor sensed that the object (eg. finger) is within the "sweet" range: 120-180, "Sweet" will be printed. The performance can be seen from the gif.
![a](https://github.com/ZhijingY/ese5190-2022-lab1-firefly/blob/main/zyao_4.4.gif)


RP2040 is connected to the PC via USB, and communicates with the sensor APDS9960 using I2C. Once the sensor detects an object approaching, it will send back the value of proximity and then RP2040 will decide what to print based on the proximity received. RP2040 uses keyboard library and object to print specific strings. The connection can be seen from the diagram called zyao_lab1.jpg.
![a](https://github.com/ZhijingY/ese5190-2022-lab1-firefly/blob/main/zyao_lab1_updated.png)

University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1


    Xiayu Zeng
        xiayu027@seas.upenn.edu
    Tested on: MacBook Air (13-inch, 2020), macOS Monterey 12.5


# Part 3:
In part 3, we use APDS9960 to detect color and display the detection results on RP2040. 
We enable the color detection function on APDS9960 and store the data in r, g, b and c, which represent red, green, blue and clear data detected by APDS9960’s sensor respectively.
To display APDS9960’s sensor readings in real time, we have to change the number of samples for each sensor reading. In APDS9960’s data sheet, it shows that the value of color_integration_time determines time between readings. The default value is 256 and we could set this value small to speed up the sensor readings.


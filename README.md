University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

<h4>JOYENDRA ROY BISWAS</h4>
[Website](https://joyendra.github.io/)
[LinkedIn](https://www.linkedin.com/in/joyendra-roy-biswas/)
Tested on: Lenovo Ideapad 320, Windows 10

<h4> README </h4>
Welcome to README of ESE 5190 Lab 1 - Firefly. In this lab, the primary objective was to familiarize ourselves with the RP2040 based board from Adafruit called [QTPy](https://learn.adafruit.com/adafruit-qt-py-2040) and interface the [APDS9960](https://cdn.sparkfun.com/assets/learn_tutorials/3/2/1/Avago-APDS-9960-datasheet.pdf) with it using I2C.
Part 1-3 mainly served as introductory blocks for [CircuitPython](https://learn.adafruit.com/adafruit-qt-py-2040/circuitpython) firmware setup, blinking on-board Neopixel LED and reading sensor values.
<h3>Section 3.2 - Firefly</h3>
In this section, we were supposed to mimic a [firefly](https://youtu.be/BtCGtaMrBXQ?t=413) by changing the NeoPixel's brightness in accordance to that of the firefly. For this we:-
    1. Imported the python libraries to read sensor data through the I2C channel.
    2. Once we received the values of r, g, b and c, we found out that the range was [0, 65535] in increasing order of intensity for each color and clear segments.
    3. Since the brightness range was from [0, 1], we decided to normalize the 'c' value by dividing it by 65535. This normalized value would then be mapped on a scale of [0, 255] as that's the range over which a pixel value is observed.
    4. The value obtained in step 4 is used to populate the pixel values of r, g and b over the range so that the brightness so obtained can be mimicked. This could also have been done using pixel.brightness(c/65535) but would have resulted in uniform value.
    5. The sensor reads values for an infinite loop and tests against the threshold to switch the LED on or off. The function described in step 4 is invoked when the threshold is exceeded giving rise to the firefly like action.

![Firefly_QtPy](https://user-images.githubusercontent.com/36339255/192074456-e15d11e9-b482-4840-95f1-5878095fd79b.gif)

<h3>Section 4.4 - "O" Scope</h3>
After being acquainted with HID components of CircuitPython, it was out turn to use the sensor data to manipulate our system keyboard to replicate some keystrokes. Initially we used the the same logic in **Section 3.2** to set a threshold and print "O" if the value was over it, else _BACKSPACE_ it from the display. The logic can be demonstrated as using the following flowchart. 

![4 4_flowchart](https://user-images.githubusercontent.com/36339255/192074641-af4bc994-208d-4d38-96e9-0c2181080d9a.jpg)

    1. The setup was initialized similar to Section 3.2
    2. The values was bucketed into categories of [DIM, BRIGHT, BRIGHTER, BRIGHTEST, BURNT RETINAS] based on the intensity of white light shone on the sensor.
    3. The values thus obtained in Step 2 were displayed on the monitor of the host device.
    
![QtPy_BrightMeasure](https://user-images.githubusercontent.com/36339255/192075004-ae4fdb8e-6236-4700-a00b-5337754b7433.gif)

Hence, these **4** exercises culminate the work of Lab 1.

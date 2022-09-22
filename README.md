University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Yuxuan Li
        liyux@seas.upenn.edu
        https://www.linkedin.com/in/yuxuan-li-26511b203/
    Tested on:  OMEN Laptop 15-ek0xxx, Windows-10 Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz   2.59 GHz
    Partner: Yuxin Wang, Xingqi Pan
# Lab description
For this lab session:  
- The MCU Adafruit QT Py RP2040 is set up and connected with the APDS99560 sensor board.
- Conduct the color regcognition and the display task with neopixel library
- The sensor can conduct brightness, gesture and color perception.
- The sensor can interactive with PC and act as the mouse and keyboard.
# Embedded Diagram
![](https://github.com/Yuxuan-Li295/ese5190-2022-lab1-firefly/blob/main/Media/Lab1_System_Overview.jpg)
# Lab demo
1. **Firefly Visualizer(Q 3.2)**:  

*APDS9960* is used to detect the light from the video 'Firefly', the light is changed synchronically via the RED LED light in the *RP2040* board.  
Since the sensor react slowly to the default sampling rate of the color sensor, so we increase the sensor's sampling rate at this part in order to have a real-time perception of the color with:   
```python
sensor.color_integration_time = 10
```
![](https://media.giphy.com/media/UAECYJoWlVC3JI4xSX/giphy.gif)  

2. Part 4: "O SCOPE"  

For this part, the brightness is visualized by using the keyboard output and the rule for change is defined as follows:
**Rule for the change**:  

    1. If the light intensity is higher than the previous one, *RP2040* will type a 'o' on the screen.
    2. If the light intensity is lower than the previous one, *RP2040* will conduct backspace operation and delete the corresponding character on the screen.
    3. If the light intensity is in the reasonable range, nothing will happen.  

An example of the output of the brightness and previous britness value are shown as follows:
![](https://github.com/Yuxuan-Li295/ese5190-2022-lab1-firefly/blob/main/Media/Output_For_Lightintensity_Data.jpg)

For part 4.3, the corresponding display is shown as follows:  
![](https://github.com/Yuxuan-Li295/ese5190-2022-lab1-firefly/blob/main/Media/4_3.gif)  

4. **Keyboard Custom Visualizer(Q 4.4)**:  

The light intensity is detected via the color sensor channel 'c' in the *RP2040* board after initialization.  
```python
from adafruit_apds9960.apds9960 import APDS9960
apds = APDS9960(i2c)
```
The Adafruit QT Py2040 is connected with APDS9960.  
PC is used to receive the infstructions and take corresponding actions.  

My visualizer provides a cool indicator of the light intensity of the surroundings.

The parameter integration time is set to be 16, and at this case the brightness value's level range for APDS9960 can be obtained as:
1025*16 = 16400.

**Small Game Rule**:  

    1. System print the hint to interact with the user to let the user open or close the flashlight.  
    
    2. The system will continue if the user have succesfully complete the option.  
    
    3. If the light intensity is greater, keyboard will print "Good Closer" and the light in the APDS9960 will change to green.  
    
    4. If the light intensity is weaker, keyboard will print “Good further” and the light in the APDS9960 will change to blue.  
    
    5. The game will automatically stop after 4 rounds of open operation.

![](https://github.com/Yuxuan-Li295/ese5190-2022-lab1-firefly/blob/main/Media/Diagram%20for%204.4.jpg)
    
![](https://github.com/Yuxuan-Li295/ese5190-2022-lab1-firefly/blob/main/Media/4_4.gif)  

# Code
[**Code: Part3.py**]: Firefly  

[**Code: Part4.3.py**]: Interact with keyboard to print 'o' and backspace  

[**Code: Part4.4.py**]: Have fun with the real-time visualizer

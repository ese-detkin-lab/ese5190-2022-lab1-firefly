University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    SURAJ SREE BALAKRISHNA MARTHY
        https://www.linkedin.com/in/suraj-marthy-8b7109138/ ; 
    Tested on: Acer Predator Helios 300 PH315-51 (15.6 inches, Intel Core i5+8th Gen), Windows 11

#README

## ESE 5190 LAB 1 : Firefly assignment performed with my groupmate - @koushik-sss

#### This repository contains three .py files: Firefly Visualizer, Custom Visualizer and Mouse Controller.

### 3.2: Firefly Visualizer

The color sensor identifies the color variations from the input and converts it to an equivalent representation from 0 to 1025 for each channel. (apds.color_integration_time) with a sampling time gap of 2.78 ms. This value is passed on to the onboard neopixel LED. The LED simulates the color changes from the firefly are reflected in the LED output.

Link to GIF:
![Firefly](https://user-images.githubusercontent.com/69215958/192077800-acc86aa7-01ea-45fa-b461-7f2de607d5eb.gif)

----

### 4.4: Custom Visualizer
![BLOCK DIAGRAM](https://user-images.githubusercontent.com/64246696/192074022-b836bd6d-0250-4ef9-8798-abe9d57f3f29.png)

The user adjusts the ambient brightness levels, which are identified by the photo-sensor, which transmits these values over the I2C interface via the stemma cable. The RP 2040 then compares the brightness levels and determines the keystrokes, which are passed to the computer via the USB-HID interface. These changes can then be observed on the text editor.

Link to GIF:
![CustomVisualizer_custom](https://user-images.githubusercontent.com/69215958/192077909-0b2e79fb-6aa8-4e38-bd4f-f20fadc3fc73.gif)

----

### 3.2: Mouse Controller

The illumination on the photo-sensor of the APDS9960 board is mapped against the X-Axis movement of the mouse. If the illumination around the sensor is bright, the cursor moves towards the right by 2 units per signal. Similarly, if it is dark, the mouse cursor moves towards the left by 2 units per signal.

Link to GIF:
![MouseControllercompress](https://user-images.githubusercontent.com/69215958/192077963-8cf9898e-bdcf-4e38-8504-40f88b7d379d.gif)

---

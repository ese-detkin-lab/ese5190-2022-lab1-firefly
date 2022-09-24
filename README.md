**University of Pennsylvania, ESE5190: Intro to Embedded Systems, Lab1**

Minghui Ni

[Minghui's LinkedIn Profile](https://www.linkedin.com/in/minghui-ni/)

Tested on: Gigabyte G5 KD, Windows 11 home 21H2

## Lab output video

Gif of the firefly visualizer from 3.2:

![image](https://github.com/minghuin/ese5190-2022-lab1-firefly/blob/main/lab1video1.gif)



Gif of the custom visualizer from 4.4:

![image](https://github.com/minghuin/ese5190-2022-lab1-firefly/blob/main/4.4video.gif)



## Overview of our visualizer from 4.4

1. Light Controlled Keyboard Input is achieved by connecting Adafruit QT Py RP2040 and APDS9960. 
2. The PC will communicate with the Adafruit board through serial communication connection.
3. We use the clear data obtained from the APDS9960 to control the HID keyboard. To be more detailed, the differential clear data is used to control the keyboard input. On the one hand, once the APDS9960 detects a increasment of brightness, character “o” would be printed through the HID keyboard. On the other hand, once the APDS9960 detects a decreasement of brightness, character “i” would be printed through the HID keyboard.
4. The APDS9960 will check the variance of the brightness once for every 0.01 second. it will calculate the differential value based on the brightness level from last time and the current brightness value, makes a decision of the output based on this differential value and finally update the brightness value record for the next time.
5. We are using the firefly video to demonstrate its functionality and its live update ability.



## Diagram of our embedded system from 4.4

The interaction between user and each components is shown in the diagram below.

<img width="1504" src="https://github.com/minghuin/ese5190-2022-lab1-firefly/blob/main/diagram_of_lab_1.jpg">

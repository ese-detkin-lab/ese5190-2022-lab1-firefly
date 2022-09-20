# ESE519-Lab1

## Team 

Yizhe Wang & Minghui Ni

[Minghui's LinkedIn Profile](https://www.linkedin.com/in/minghui-ni/)

Tested on: Gigabyte G5 KD, Windows 11 home 21H2

## Lab output video

Gif of the firefly visualizer from 3.2:

![image](https://github.com/minghuin/ese5190-2022-lab1-firefly/blob/main/lab1video1.gif)



Gif of the custom visualizer from 4.4:

![image](https://github.com/minghuin/ese5190-2022-lab1-firefly/blob/main/4.4video.gif)



## Overview of our visualizer from 4.4

1. Light Controlled Keyboard Input is achieved by connecting Adafruit QT Py RP2040 and APDS 9600. 
2. The PC will communicate with the Adafruit board through serial communication connection.
3. We use the clear data obtained from the APDS 9600 to control the HID keyboard. On the one hand, when the light received by the sensor is brighter, character “O” would be printed through the HID keyboard. On the other hand, when the light becomes weaker, character “I” would be printed through the HID keyboard. 
4. We are using the firefly video to demonstrate its functionality and its live update ability



## Diagram of our embedded system from 4.4

The interaction between user and each components is shown in the diagram below.

<img width="1504" alt="WeChat7f757e794df59be7fbc2de05c5f66f7c" src="https://user-images.githubusercontent.com/114015725/191332983-37bab0b9-2005-4332-ab65-120983f8fb5b.png">

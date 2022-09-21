# University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Yu Feng
    University of Pennsylvania, ESE5190: Intro to Embedded Systems, Lab 1
    Tested on:  MacBook Pro (15-inch, 2018), macOS Monterey 12.4


# Demo Video For Section 3.2
1. https://github.com/skyfall88888/Lab-1-Yu-Feng/blob/main/3.2_demo_1.gif
2. https://github.com/skyfall88888/Lab-1-Yu-Feng/blob/main/3.2_demo_2.gif

# Overview of Lab 1 Section 4.4

I implemented a real-time color information display. The instant color intensity of R, G, B and C will be displayed. The APDS 9960 picks up the lighting and sends the R, G, B and C values to the RP 2040 where it utilized the HID to display these information on the screen. From the demo video (44_demo.gif) it can be seen that the readings for R, G, B and C change with the lighting condition. 

Code for section 4.4:
https://github.com/skyfall88888/Lab-1-Yu-Feng/blob/main/lab1_44_code.py

Demo Video for section 4.4:
https://github.com/skyfall88888/Lab-1-Yu-Feng/blob/main/4.4_demo.gif

Below is an illustrative figure of the general structure of the embedded system. Dipicted in purple represents the lighting. Arrowed lines in both directions represent the communication protocol between the two devices. For example, for communicating between APDS9960 and RP2040, I2C protocol is implemented.

![IMG_0407](https://user-images.githubusercontent.com/95589555/191562904-eff736a3-582e-4a37-bade-cc54c11bd96a.jpg)

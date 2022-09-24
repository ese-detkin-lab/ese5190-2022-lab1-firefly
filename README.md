University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

Shantanu Sampath
Worked with: Aamir Khambaty

https://www.linkedin.com/in/shantanu-sampath/
Tested on: HP 17 Windows 11

Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

4.4 Visualiser:
Create a real time brightness visualiser to detect the intensity of light in the room and report it onto the console. 
The APDS9960 sensor detects the brightness of light falling onto it. The Adafruit QT- Py 2040 MCU sends text commands to show the level of brightness on the screen. THe brightness is indicated by the number of "=" displayed. As the brightness increases upto the hard cap of 1000, we see the indicators rising. If brightness gets dimmer, the Raspberry Pi sends "backspaces" to the console to reduce the number of "=" displayed. 

Video and block diagram of the visualizer is included in the repo. 

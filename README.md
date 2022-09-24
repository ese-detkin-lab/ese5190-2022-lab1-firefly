University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

Aamir Abbas Khambaty Worked with: Shantanu Sampath

https://www.linkedin.com/in/aamir-khambaty-7807a11a4/

Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

4.4 Visualiser: Create a real time brightness visualiser to detect the intensity of light in the room and report it onto the console. The APDS9960 sensor detects the brightness of light falling onto it. The Adafruit QT-PY 2040 microcontroller board reads the information from the ADPS9960 via I2C protocol and then correspondingly  sends text commands to show the level of brightness on the screen. THe brightness is indicated by the number of "=" displayed. As the brightness increases upto the hard cap of 1000, we see the indicators rising. If brightness gets dimmer, the RPi 2040 sends "backspaces" to the console to reduce the number of "=" displayed.
this process is further demonstarted by use of a flashlight. 

Video and block diagram of the visualizer is included in the repo.

University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Rongqian Chen
        chenrongqian.com
    Tested on: Alienware m15 R2, Windows 10

Include lab questions, screenshots, analysis, etc. s public, so don't put anything here you don't want to share with the world.)

The firefly visualizer uses the RGB sensor which returns the light's R,G,B and clarity value, which range from 0-65536(depend on the clock circle you setup). Then set the neopixel.brightness with a scaling clarity value(scaling to 0~1). Then the LED on RP2040 will follow the brightness of light the sensor received. The firefly LED will be looks like this:


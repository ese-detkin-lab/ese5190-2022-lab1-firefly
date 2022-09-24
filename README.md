University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Rongqian Chen
        chenrongqian.com
    Tested on: Alienware m15 R2, Windows 10

Include lab questions, screenshots, analysis, etc. s public, so don't put anything here you don't want to share with the world.)

The firefly visualizer from 3.2 uses the RGB sensor which returns the light's R,G,B and clarity value, which range from 0-65536(depend on the clock circle you setup). Then set the neopixel.brightness with a scaling clarity value(scaling to 0~1). Then the LED on RP2040 will follow the brightness of light the sensor received. The firefly LED will be looks like this:

![firefly_AdobeExpress](https://user-images.githubusercontent.com/43904091/192077234-17ec125b-c478-4bef-82cf-f0a4f32a7157.gif)

For 4.4, I designed a real-time visualizer using RGB sensor and LED. The program first read the light's color and return rgb values, then the LED will show the same color sensor detected, and the test displayer will output the largest value among three colors. The test result is shown as following.

![rgb_AdobeExpress](https://user-images.githubusercontent.com/43904091/192077974-05f6d2e4-9393-4dfe-a4e1-a800f2c7f306.gif)

The diagram of my embedded system includes:

![519 picture](https://user-images.githubusercontent.com/43904091/192078595-5930c43d-1e35-456d-ad7c-67e9390761e7.jpg)

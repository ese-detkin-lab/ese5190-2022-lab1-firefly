University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Yuxuan Li
        https://www.linkedin.com/in/yuxuan-li-26511b203/
    Tested on:  OMEN Laptop 15-ek0xxx, Windows-10

(TODO: Your README)
1. Firefly Visualizer(Q 3.2):
*APDS9960* is used to detect the light from the video 'Firefly', the light is changed synchronically via the RED LED light in the *RP2040* board.

2. Keyboard Visualizer(Q 4.4):
The light intensity is detected via the color sensor channel 'c' in the *RP2040* board. The Adafruit QT Py2040 is connected with APDS9960. My visualizer provides a cool indicator of the light intensity of the surroundings.

The parameter integration time is set to be 16, and at this case the brightness value's level range for APDS9960 can be obtained as:
1025*16 = 16400.

**Rule for the change**:
    1. If the light intensity is higher than the previous one, *RP2040* will type a 'o' on the screen.
    2. If the light intensity is lower than the previous one, *RP2040* will conduct backspace operation and delete the corresponding character on the screen.
    3. If the light intensity is in the reasonable range, nothing will happen.
**Small Game Rule**:
    1. System print the hint to interact with the user to let the user open or close the flashlight.
    2. The system will continue if the user have succesfully complete the option.
    3. The game will automatically stop after 4 rounds of open operation.



Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

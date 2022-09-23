University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Ruturaj A. Nanoti and Siddhant Mathur
        www.linkedin.com/in/ruturajn | www.linkedin.com/in/siddhantmathur14
    Tested on: ASUS TUF DASH F15, Windows 11 | HP Pavilion X360, Windows 10

## General Information
- The [hid_keyboard](https://github.com/Ruturajn/ese5190-2022-lab1-firefly/tree/main/hid_keyboard) directory contains the code for **Q4.4**. Our program emulates
    a keyboard, based on the brightness values and gesture control using the *APDS9960* (The Color/Proximity/Gesture sensor). This directory also contains, all
    the libraries associated with the code, all placed in the `lib` folder.
- The [firefly](https://github.com/Ruturajn/ese5190-2022-lab1-firefly/tree/main/firefly) directory contains the code for **Q3.2**, in which the *blue* LED on the 
    *RP2040* dims, and brightens based on the brightness value obtained from *APDS9960*. As stated above, all the librabries used are placed under the `lib` directory.
- All the other directories follow the same organization, of libraries and code.

## Walkthrough

### Firefly - Q3.2

- This program takes in the brightness values from the *APDS9960* and scales it down from a range of *0 - 65536* to *0 - 255*.
- The scaling is done to pass the brightness value to the *blue* LED, on the *RP2040*.
- Also, the `color_integration_time` property is tweaked to decrease the number of samples for each reading, which decreases the time between
    two sensor readings, and hence provides a faster response, although this does reduce the accuracy of the readings a bit, and that is a trade-off
    which needs to be worked with, based on the desired result.
- Depending on the brightness, the LED changes from a dimmed state to a bright state, and vice-versa.
- Finally, when the firefly video is played in front of the sensor, the LED replicates the changes observed in the video.


### Keyboard Emulator - Q4.4

- In this program, the *RP2040* was programmed to emulate a keyboard.
- Firstly, we acquire the brightness data from the *APDS9960* and scale it down from a range of *0 - 65536* to *0 - 255*.
- Then, if the brightness value is between `0` and `100`. We print out the statement `This is very Dim!!\n`. The `\n` character
    at the end, places the cursor on a newline.
- If the above condition is not satisfied, we check if the brightness is within the range of `100` to `190`. If so, then the
    `BACKSPACE` action is sent.
- While all of the above steps are running, simulataneously we are also checking if the user waves their hand, leftwards or rightwards
    (i.e. the gesture sensor returns `4` or `3`) on the sensor. This action is encoded to *quit* the program, and hence the execution stops.

## Flow Diagram
![](/assets/Diagram.png)

## GIFs

### Firefly

![](/assets/firefly.gif)

### Keyboard Emulator

![](/assets/Q4_LAB1.gif)

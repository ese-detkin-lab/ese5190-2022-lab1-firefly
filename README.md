University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Qi Xue
    Tested on: Alienware x15 R1, Windows 11 Home, 11th Gen Intel(R) Core(TM) i7-11800H

## Problem3 Firefly visualization

  ![image](https://github.com/sueqixue/ese5190-2022-lab1-firefly/blob/main/Media/p_3.gif)

## Problem4 Keyboard visualization

  ![image](https://github.com/sueqixue/ese5190-2022-lab1-firefly/blob/main/Media/p_4.gif)

  I set the color integration time to 50 and set a safe value 200 to ensure the sensor would not be affected by the environment too much. I also introduced an initial sensing point by check if the brightness was larget than 300 to assist me to stop the program easily when I wanted to. As you can see in the gif, when the Clear (brightness) value significantly increased, the sensor would control the keyboard of my pc to type O; when the Clear (brightness) value significantly decreased, the sensor would control the keyboard of my pc to type the backspace, thus the O was deleted.

  A diagram of my embbedded system is shown below:

  ![image](https://github.com/sueqixue/ese5190-2022-lab1-firefly/blob/main/Media/p_4_diagram.jpg)

  My system works as follows:
  
  1. Run the code, and turn on the light;
  2. Press the ‘+’ button of the light, we can see O was typed;
  3. Press the '-' button of the light, we can see O was deleted;
  4. Trun off the light so no input will be take.

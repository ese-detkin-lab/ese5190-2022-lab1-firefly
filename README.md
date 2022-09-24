University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Haoliang You
       haolyou@seas.upenn.edu
    Tested on: ROG Zephyrus (16-inch, 2022), Windows 11

Part 3

3.2 ADPS 9960 senses the change in brightness of the external light, and reflects the change on RP 2040. I tested its performance using the YouTube video provided by the professor and found that it works well as shown below.

Actual experimental effect

![a](https://github.com/HaoliangYou/ese5190-2022-lab1-firefly/blob/main/3.2.gif)

Part 4

4.3 After adding the corresponding library, I use the "keyboard" to input "o" when the sensor senses that the brightness of the external light increases. Correspondingly, the "keyboard" input "backspace" when the brightness decreases. It's worth noting that I set the decision condition for program termination. In the case of setting a certain error, when the light intensity is much lower than the intensity of ambient light and the test light, the test will be terminated.

Diagram of this system

![a](https://github.com/HaoliangYou/ese5190-2022-lab1-firefly/blob/main/4.3.jpg)

Actual experimental effect

![a](https://github.com/HaoliangYou/ese5190-2022-lab1-firefly/blob/main/4.3.gif)


4.4 On the basis of the above experiments, for more creations, we can use the proximity, direction, etc. I use the direction monitoring function myself. The "keyboard" will output the detected direction. Based on the current ambient light intensity and the direction recognized by APDS 9960, the RP2040 outputs the corresponding light of different colors. In my imagination, this experiment can be applied to various fields such as detection and warning, information reminder and so on.

Diagram of this system

![a](https://github.com/HaoliangYou/ese5190-2022-lab1-firefly/blob/main/4.4.jpg?raw=true)

Actual experimental effect

![a](https://github.com/HaoliangYou/ese5190-2022-lab1-firefly/blob/main/4.4.gif)

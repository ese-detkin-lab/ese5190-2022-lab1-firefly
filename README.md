University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Haoliang You
       haolyou@seas.upenn.edu
    Tested on: ROG Zephyrus (16-inch, 2022), Windows 11

Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

3.2 ADPS 9960 senses the change in brightness of the external light, and reflects the change on RP 2040.

Actual experimental effect

![a](https://github.com/HaoliangYou/ese5190-2022-lab1-firefly/blob/main/3.2.gif)

4.3 After adding the corresponding library, I use the "keyboard" to input "o" when the sensor senses that the brightness of the external light increases. Correspondingly, the "keyboard" input "backspace" when the brightness decreases.

Diagram of this system

![a](https://github.com/HaoliangYou/ese5190-2022-lab1-firefly/blob/main/4.3.jpg)

Actual experimental effect

![a](https://github.com/HaoliangYou/ese5190-2022-lab1-firefly/blob/main/4.3.gif)


4.4 On the basis of the above experiments， for more creations, we can use the proximity, direction, etc. I use the direction monitoring function myself. I use the "keyboard" to output the detected direction, and based on the current ambient light intensity, the RP2040 outputs the corresponding light of different colors.

Diagram of this system

![a](https://github.com/HaoliangYou/ese5190-2022-lab1-firefly/blob/main/4.4.jpg?raw=true)

Actual experimental effect

![a](https://github.com/HaoliangYou/ese5190-2022-lab1-firefly/blob/main/4.4.gif)

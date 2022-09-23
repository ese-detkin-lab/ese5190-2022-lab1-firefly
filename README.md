University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    (TODO) Siyun Wang
        

(TODO: Your README)

Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

3.2 When the brightness of the lights on the screen changes, the brightness of the leds on the RP2040 also changes.
![a](https://github.com/Phoebe-www/ese5190-2022-lab1-firefly/blob/main/ezgif.com-gif-maker%20(2).gif?raw=true)

4.4 RP2040 and APDS9960 connected via I2C, PC and RP2040 connected via USB. The RP2040 used keyboard library to a output specific string. And my idea is when the hand is close to the LED on the RP2040, the string "Phoebe" is output, and when the hand is moved away and the apds.proximity is more than 100, the output is stopped.

![a](https://github.com/Phoebe-www/ese5190-2022-lab1-firefly/blob/main/ezgif.com-gif-maker%20(1).gif?raw=true)


Diagram of the embedded system

![a](https://github.com/Phoebe-www/ese5190-2022-lab1-firefly/blob/main/diagram.PNG?raw=true)

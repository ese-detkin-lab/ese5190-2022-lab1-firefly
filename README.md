# University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Ronil Synghal
        Personal Website: https://ronilsynghal.com
        LinkedIn: www.linkedin.com/in/ronil-synghal
    Tested on: MacBook Pro (13-inch, 2018, Four Thunderbolt 3 Ports), macOS Big Sur 11.4

## Firefly
For this part of the lab the goal was to program the embedded system so that its RGB LED tracks the brightness reading from its color sensor. In order to test the output, we utilzied a video of a firefly flashing. A demo of this project can be seen below.

![](https://github.com/ronils428/ese5190-2022-lab1-firefly/blob/main/firefly.gif)


## Visualizer
The second part of the lab was to create a custom real-time visualizer. Being the huge Game of Thrones fan that I am, I decided to create a visualizer that would print a quote from the show. The steps for this visualizer are as follows:
1. Shine a light over the sensor on the ADPDS9960. 
2. If the brightness exceeds a certain value than the LED on the RP2040 will change from Red to Green
3. The embedded system will use your keyboard to output a quote from Game of Thrones. When the LED is Red, the embedded system will be deleting characters. 
4. The program automatically terminates when the entire quote has been outputted.

A diagram of the visualizer can be found below:

![](https://github.com/ronils428/ese5190-2022-lab1-firefly/blob/main/visualizerDiagram.jpg)

Here is a gif of the visualizer in action. 

![](https://github.com/ronils428/ese5190-2022-lab1-firefly/blob/main/visualizer.gif)

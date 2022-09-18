University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Junpeng Zhao
         https://Pretendtohavealink.com/

    Tested on: XPS13 9370, Windows10 Pro 21H2

## Firefly visualizer
![firefly](https://github.com/PZZ97/ese5190-2022-lab1-firefly/blob/main/media/dim.gif?raw=true)
## custom visualizer from 4.4
![custom](https://github.com/PZZ97/ese5190-2022-lab1-firefly/blob/main/media/keyboard.gif?raw=true)

The integration time was set to 16, which means the MAXIMUM brightness value read from APDS9960=1025*16=16400. However, the expeiment showed that the effective brightness range differs and in my case, I set the tolerance to 200.

It works as follows:

1. First, press any key to start
2. let the sensor towards the ground so as to acquire the lowest brightness, then rotate it to be vetical so now we acqure the first letter.
3. after that we can continue to rotate so that acquire the maximum brightness value and now we can get the sencond letter. 
4. rotate in opposite so we can delete letters. 
5. Totally cover the sensor so to end up input
![diagram](https://raw.githubusercontent.com/PZZ97/ese5190-2022-lab1-firefly/main/media/diagram.jpg)

![image](https://github.com/PZZ97/ese5190-2022-lab1-firefly/blob/main/media/serialoutput.png?raw=true)




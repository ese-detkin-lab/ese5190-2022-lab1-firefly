University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Harish Ramesh, Sugata Sen
        https://www.linkedin.com/in/harishramesh1998/ ; https://www.linkedin.com/in/sugata-sen/
    Tested on: Lenovo Legion Slim-7, Windows-11; ASUS ROG GL-552 VW, Windows-10
    
## 1. Outputs
### Firefly Visualizer (Q.3.2):

![](https://github.com/harishramesh98/ese5190-2022-lab1-firefly/blob/4b13ff770cce6840b5cc92c0ef00e4e42ec17038/firefly.gif)

### Keyboard Visualizer (Q.4.4):

![](https://github.com/harishramesh98/ese5190-2022-lab1-firefly/blob/4b13ff770cce6840b5cc92c0ef00e4e42ec17038/keyboard.gif)

## 2. Overview of 3.2
The color sensor of ADPS9960 is initially set to integration time of apds.color_integration_time=256, which is too slow of a response for the purpose of a firefly follower, so we set it to apds.color_integration_time=1 to make the color sensor react as fast as possible to the external light source.

Now, we simply scale the cumulative/brightness data from sensor, and scale it for visibility before using it to modulate the brightness of the on-chip LED of the RP2040. We have chosen the Red colour to output, but any combination of colours can be chosen as long as their brightnesses are proportional to "c". Where "c" is the brightness/luminosity data of the APDS9960 color sensor.

Reacts accordingly when shown to the youtube video of a firefly:

    Upon sensing a bright flash , LED gets brighter
    Upon sensing less light, LED gets dimmer


## 3. Overview of 4.4
The ADPS9960 sensor receives input from user via various stimuli. In our implementation we have taken advantage of its proximity sensor and its ability to detect colour.
The RP2040 was programmed to detect the following and react accordingly:

* Upon startup, the message '**waiting to type**', will appear on the serial output/terminal.
* In the case of an **upward motion**, print the letter '**a**'.
* In the case of a motion towards the **right**, the letter '**b**'.
* In the case of a **downward motion**, the letter '**c**'.
* In the case of a motion to the **left**, the letter '**d**'.
* In the case of **red light**, to enable a **backspace**.
* In the case of a **blue light**, to **break and exit the program**.


## 4. Diagram of embedded system.
![diagram of the embedded system used](https://github.com/harishramesh98/ese5190-2022-lab1-firefly/blob/f69d275f3e1db8cf3439e5f79bddcecebff8c354/Embedded_system_block_diagram.jpeg)



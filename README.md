University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Sugata Sen, Harish Ramesh
        https://www.linkedin.com/in/sugata-sen/ ; https://www.linkedin.com/in/harishramesh1998/
    Tested on:  ASUS ROG GL-552 VW, Windows-10 ; Lenovo Legion Slim-7, Windows-11
    
## 1. Outputs
### Firefly Visualizer (Q.3.2):

![](https://github.com/sugahiraeth/ese5190-2022-lab1-firefly/blob/5843eca5bdbd3ccc6588ffdb30495b5fbd8118fb/firefly.gif)

### Keyboard Visualizer (Q.4.4):

![](https://github.com/sugahiraeth/ese5190-2022-lab1-firefly/blob/5843eca5bdbd3ccc6588ffdb30495b5fbd8118fb/keyboard.gif)

## 2. Overview of 4.4
The ADPS9960 sensor receives input from user via various stimuli. In our implementation we have taken advantage of its proximity sensor and its ability to detect colour.
The RP2040 was programmed to detect the following and react accordingly:

* Upon startup, the message '**waiting to type**', will appear on the serial output/terminal.
* In the case of an **upward motion**, print the letter '**a**'.
* In the case of a motion towards the **right**, the letter '**b**'.
* In the case of a **downward motion**, the letter '**c**'.
* In the case of a motion to the **left**, the letter '**d**'.
* In the case of **red light**, to enable a **backspace**.
* In the case of a **blue light**, to **break and exit the program**.


## 3. Diagram of embedded system.
![diagram of the embedded system used](https://github.com/sugahiraeth/ese5190-2022-lab1-firefly/blob/5843eca5bdbd3ccc6588ffdb30495b5fbd8118fb/Embedded_system_block_diagram.jpeg)


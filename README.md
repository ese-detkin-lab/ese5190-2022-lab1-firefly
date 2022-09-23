University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

     Sen Luo
        email: luosen@seas.upenn.edu
        Tested on: Razer Blade 15 (15-inch, 2020), Windows 10 21H2

# 3.2 FIREFLY
![](https://github.com/SEN316/ese5190-2022-lab1-firefly/blob/main/3.2.gif)

In part 3.2, we track the brightness of screen by using the RP2040 board and the photodiodes on the APDS9960. We program the embedded system in order to make its RGB LED tracks the brightness reading from its color sensor. We use vieo (https://youtu.be/BtCGtaMrBXQ?t=413) to test the embedded system and the gif above shows that the board flash sync with the firefly. 

# 4.4 Real-time Visualizer
![](https://github.com/SEN316/ese5190-2022-lab1-firefly/blob/main/4.4.gif)

In part 4.4, I design a program to print "bright" when the brightness increases, and print "dim" when the brightness decreases. Also, it can type the letter "L" when the brightness reading of green increases, and type the letter "S" when the brightness reading of green decreases. And if the sensor senses the red light, the main loop will break. In the gif video above, I use video (https://youtu.be/BtCGtaMrBXQ?t=413) to test the function of code. 

![](https://github.com/SEN316/ese5190-2022-lab1-firefly/blob/main/4.4.jpg)

After the sensor is pointed to the video, the sensor will detect the brightness reading of the video and record it value as c in loop. If the brightness reading is larger than the stored value c, the program of RP2040 will print the string "bright". Otherwise, if the brightness reading is smaller than the stored value c, the program of RP2040 will print the string "dim". In same logic, the change of brightness reading of green will make RP2040 type the letter "L" or "S". The whole program has an 
escape hatch' where it breaks out of the main loop when it senses the brightness of red larger than 1000.

Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)


University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    (TODO) Chenye Xiong
        (TODO) Email: xcyxcy@seas.upenn.edu
    Tested on: ThinkPad XI Carbon 5th Signature Edition, Windows 10
(TODO: Chenye Xiong)

Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)
## Lab1 3.2 The board should flash in sync with the firefly
1. Using the color sensor to detect the value of color intensity at different times
2. Subtract the value at the previous time from the value at the next time, and define this difference as 'k'
3. If k>=0, the LED doesn't get bright and if k<0, the LED turns bright
   the gif of the result: 
<div align=center>
<img src="https://github.com/xcyxcyxcyxcy/ese5190-2022-lab1-firefly/blob/main/ezgif.com-gif-maker%20firefly.gif" width="420" >  
</div>

### The code:
<div align=center>
< img src=https://github.com/xcyxcyxcyxcy/ese5190-2022-lab1-firefly/blob/main/ezgif.com-gif-maker.gif >  
</div>

### question: 
The board reacts much slower than the firefly

## Lab1 4.4 The display should update in “real time” along with your sensor
Description: When the sensor senses color, it board will control the keyboard to type the name of this color on the screen.
1. Find the maximum of each value of each color intensity
2. Find the color corresponding to the maximum value
3. The board controls the keyboard to type the name of this color on the screen

### The code:
<div align=center>
< img src=https://github.com/xcyxcyxcyxcy/ese5190-2022-lab1-firefly/blob/main/ezgif.com-gif-maker.gif >  
</div>

### The gif of the result: 
<div align=center>
< img src=https://github.com/xcyxcyxcyxcy/ese5190-2022-lab1-firefly/blob/main/ezgif.com-gif-maker.gif >  
</div>

### question:
It will type red when there is no specific color close to the sensor.

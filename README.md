# University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Yuxin Wang
        https://www.linkedin.com/in/yuxin-wang-4b8800229/
    Tested on: (TODO) MacBook Pro (16-inch, 2021), macOS Monterey 12.6
    Partner: Xingqi Pan, Yuxuan Li

# What it dose
1.The color of LED will change with the ambient light (if you put the sensor close to firefly's vedio, it will flash in sync with the firefly!)
2.Your laptop will print character (like 'a', 'b') when you close to the sensor
3.Your mouse will move with your gesture (if your finger move left, the mouse will alos move left)

# Embedded Architecture
<img width="600" alt="system" src="https://user-images.githubusercontent.com/87698138/191405058-359b99c5-cec0-42bd-958d-8d8cd8c84b57.png">

# File Description
【**code(Part3.3).py**】: Change LED color with ambient light

【**code(Part4.4).py**】: Final model code

【**Final.mp4**】: Final model video

【**LED.MP4**】: LED flash in sync with firefly video

# Part4 code detail
## Distance detection and keyboard print
![LED](https://user-images.githubusercontent.com/87698138/191640161-04dbe934-9722-4e28-8a65-5aab26399df2.gif)
In this section we use distance to control the keyboard, when the value of distance is large enough (when you close to the sensor) the keyboard will print a or B.
```python
dis = apds.proximity
if dis > 100 and dis <= 210:
    print('distance is:', dis)
    keyboard.send(Keycode.A)
if dis > 210 and dis <= 220:
    keyboard.send(Keycode.SHIFT, Keycode.B)
    print('distance is:', dis)
```

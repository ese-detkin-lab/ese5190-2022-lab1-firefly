# University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Yuxin Wang
        https://www.linkedin.com/in/yuxin-wang-4b8800229/
    Tested on: (TODO) MacBook Pro (16-inch, 2021), macOS Monterey 12.6
    Partner: Xingqi Pan, Yuxuan Li

# What it does
1.The color of LED will change with the ambient light (if you put the sensor close to firefly's vedio, it will flash in sync with the firefly!)
2.Your laptop will print character (like 'a', 'b') when you close to the sensor
3.Your mouse will move with your gesture (if your finger move left, the mouse will alos move left)

# Embedded Architecture
<img width="500" alt="system" src="https://user-images.githubusercontent.com/87698138/191405058-359b99c5-cec0-42bd-958d-8d8cd8c84b57.png">

# File Description
【**code(Part3.2).py**】: Change LED color with ambient light

【**code(Part4.4).py**】: Final model code

【**Final.mp4**】: Final model video

【**LED.MP4**】: LED flash in sync with firefly video

# Code detail
## Flash with firefly
<img width="500" alt="LED" src="https://user-images.githubusercontent.com/87698138/191640161-04dbe934-9722-4e28-8a65-5aab26399df2.gif">

## Distance detection and keyboard print
<img width="500" alt="LED" src="https://user-images.githubusercontent.com/87698138/191643495-2644e8ce-8a74-4bed-bdcb-e6bc06b8a1f6.gif">

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
## Gesture control mouse
In this section we use gesture to control the mouse, when your finger move right, the mouse will move right.
<img width="500" alt="LED" src="https://user-images.githubusercontent.com/87698138/191641068-65ba78e1-693c-499a-aeae-228d3b4904ac.gif">

```python
gesture = apds.gesture()
if gesture == 1:
    mouse.move(y=80)
    print('Saw gesture: up')
if gesture == 2:
    mouse.move(y=-80)
    print('Saw gesture: down')
if gesture == 3:
    mouse.move(x=80)
    print('Saw gesture: left')
if gesture == 4:
    mouse.move(x=-80)
    print('Saw gesture: right')
```

## Light detection and sentance print
In this section we use the clear of light to print sentence, when it's too dim, the keyboard will print out: "It is too dim. please turn on the light!"

<img width="500" alt="LED" src="https://user-images.githubusercontent.com/87698138/191641797-8f989162-449d-449b-9964-af2cab0dbc3e.gif">

```python
r, g, b, c = apds.color_data
clear = c / 256
pixels.fill((clear, clear, clear))
if clear <2 :
    print("clear: ", clear)
    keyboard_layout.write('It is too dim, please turn on the light!\n')
```

## Break and Stop
When the claer of light is high enough, the while loop will break and the system will stop
```python
if clear > 220:
    print('System turn off')
    break
```

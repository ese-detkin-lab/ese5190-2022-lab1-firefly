University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Sizhe Ma
        masizhe@seas.upenn.edu
    Tested on: Thinkpad X1, Windows 10 Pro, Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz   2.11 GHz
    Partner: Sudong Wang
    
# Overview
In this lab, we mainly did several tasks list below:
1) get familiar with microcontroller Adafruit QT Py RP2040 and sensor board APDS9960
2) set up Adafruit QT Py RP2040 and connect it to APDS9960
3) get familiar with the sensor brightness perception, color recognition and gesture perception function 
4) track the brightness reading from APDS9960's color sensor and simultaneously display on RP2040's LED via neopixel (Q.3.2)
5) track the gesture and brightness reading and display on PC with RP2040's keyboard function

### code setup
```python
import board
import busio
import time
import adafruit_apds9960.apds9960
import neopixel

i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True                         # for brightness sensor
sensor.enable_color = True                             # for color sensor
sensor.enable_gesture = True                           # for gesture sensor
sensor.color_integration_time = 10                     # for a much faster source of data

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)          # for RP2040's LED display
```

# Q.3.2: Firefly Visualization
In this section, we used APDS9960 color sensor to track the brightness reading of firefly flashing, and then use RP2040's LED to simutaneously display the flashing. when the firefly goes bright, the LED should get bright, and the LED should get dim when the firefly goes dim. Then the board would flash in sync with the firefly in the video.

### Basic Logic
Firstly, we initialize a variable named c_last which indicate the brightness of least reading.

When the firefly starts flashing (goes from dim to bright), the "clear" channel reading will have a “value jump” (always above 100). So when new c (clear) value is 100 higher than the last c value, the LED will be on.

When the firefly goes from bright to dim, the new c (clear) value will be 100 lower than the last c value, and we turn off the LED.

```python
c_last = 0                                             # initialize the parameter
while True:
    r, g, b, c = sensor.color_data                     # track the reading from color sensor
    print(c)
    if c >= (c_last+100):                              # indicate that it is going bright
        pixels.fill((255, 255, 255))                   # RP2040's LED display (on)
    elif c <= (c_last-100):                            # indicate that is going dim
        pixels.fill((0, 0, 0))                         # RP2040's LED display (off)
    c_last = c
```

### Result
![](https://github.com/MaxMa6150/ese5190-2022-lab1-firefly/blob/main/firefly_visualization.gif)

RP2040's LED flashed in sync with the firefly in the video.

# Q.4.4 Keyboard Visualization
In this section, we used APDS9960 gesture perception and color sensor to control the microcontroller keyboard dispaly. Firstly, when we wave our hand in front of the sensor, RP2040 will simutaneously give "goes up/down/left/right" text display on PC. Then when we expose the sensor to a light sourse or cover it up, it will RP2040 will simutaneously give "goes bright/dark" text display on PC.

### Basic Logic
additional setup:
```python
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keys_pressed = [Keycode.O, Keycode.BACKSPACE]                 # For Q.4.3
control_key = Keycode.SHIFT                                    # For Q.4.3
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
```

Firstly, we set the integration time to 10 to have higher response rate.

For the gesture test, we use gesture perception on APDS9960 sensor. When we wave hands and our gesture is detected, sensor.gesture will return 1, 2, 3, 4 which represent up, down, left and right. 

Then the microcontroller will correspondingly display the direction of waving hands. The gesture display will run four times.

```python
while True:
    time.sleep(2)                                             # Break for user to move the mouse to text file
    info = keyboard_layout.write("Test gesture first!\n")     # Start the gesture section
    i = 0
    while i <= 3:                                             # Run the gesture test 4 times
        gesture = sensor.gesture()                            # track the reading from gesture sensor
        if gesture == 1:                                      # gesture is "up"
            info = keyboard_layout.write("Going up!\n")       # keyboard display
            time.sleep(0.1)
            i += 1
        if gesture == 2:                                      # gesture is "down"
            info = keyboard_layout.write("Going down!\n")
            time.sleep(0.1)
            i += 1
        if gesture == 3:                                      # gesture is "left"
            info = keyboard_layout.write("Going left!\n")
            time.sleep(0.1)
            i += 1
        if gesture == 4:                                      # gesture is "right"
            info = keyboard_layout.write("Going right!\n")
            time.sleep(0.1)
            i += 1
```
After four rounds of gesture display, we continue to the brightness testing. The light detecting logic is similar to Q.3.2.

After detecting the light change, the microcontroller will correspondingly display "going bright/dark".

The light test will go four rounds, then the while loop will break.


```python
    time.sleep(1)                                            # break between two sections
    info = keyboard_layout.write("Then test brightness!\n")
    i = 0
    while i <= 3:                                            # run the gesture test 3 times
        r, g, b, c = sensor.color_data                       # track the reading from color sensor
        if c >= (c_last+100):                                # indicate that it is going bright
            info = keyboard_layout.write("Going bright!\n")  # keyboard display
            time.sleep(1)                                  # break
            i += 1
        elif c <= (c_last-100):                              # indicate that it is going dark
            info = keyboard_layout.write("Going dark!\n")    
            time.sleep(1)
            i += 1
        c_last = c
    info =keyboard_layout.write("Done\n")
    break                                                    # stop testing
```
### Flow Chart
![ed1df5386e07dc228cbbfbe83dfe6f0](https://user-images.githubusercontent.com/114200453/191912913-374ec68e-20b5-4762-9f6d-bdb805208591.png)


### Result
![](https://github.com/MaxMa6150/ese5190-2022-lab1-firefly/blob/main/keyboard_visualization.gif)

### Diagram of embedded system from 4.4
![60deb0d783acc1e6003a718d1167e92](https://user-images.githubusercontent.com/114200453/191920508-ec21f8ff-f0d8-47dc-8363-e5809f412ca7.png)

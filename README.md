University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Katrina Ji
        LinkedIn: https://www.linkedin.com/in/katrina-ji-776364105/
    Tested on: MacBook Pro (14-inch, 2021), macOS Monterey 12.5.1

## Section 1 "BLINK LED"

Easy test code to make sure the board is running properly.

The blinking frequency can be altered by changing the function:
```python
time.sleep()
```

## Section 2 "SENSOR (PROXIMITY/COLOR/GESTURE)"

### The proximity result video is shown below:

https://user-images.githubusercontent.com/114244957/192000826-352c51fb-1477-4278-81bf-85b6859fcf46.mov

### The Color result is shown below:

https://user-images.githubusercontent.com/114244957/192002832-ff3e35bf-002e-4ed1-a88f-a45df752d1ca.mov

We can adjust the sampling rate of the color sensor to alter its sensitivity.
```python
apds.color_integration_time = #
```
The range is from 1 to 256.

### The Gesture result is shown below:
https://user-images.githubusercontent.com/114244957/192003645-10358efb-f69c-49d2-9937-5d7d806beef5.MOV

Notice that:
    0 = No gesture detected;
    1 = Up gesture detected;
    2 = Down gesture detected;
    3 = Left gesture detected;
    4 = Right gesture detected;
 
 There is an advanced version that keep detecting the gestures. The advanced code is used in later section.

## Section 3 "FIREFLY"

https://user-images.githubusercontent.com/114244957/192005032-9575e462-4189-4930-81bd-42f67fdcab45.mov

As we increase the sampling rate, the LED responses faster to the firefly.
The sum of the RGB is chosen even though the light of the firefly is yellow. We can also change the brightness of the LED only according to the red and green colors. However, choosing the sum of all lights can boardern the application.

## Section 4 "'O'-SCOPE"

### Section 4.2 Change cursor's position according to the change of brightness

https://user-images.githubusercontent.com/114244957/192008665-03610ff3-35b6-4875-a315-2be82404f6b8.mov

The change of light is not stable due to the influence from the ambient light. When we change from cursor to actual "O"-scope, the performace is significently better. The code is similar to "O"-scope. It will be explained in the next section.

### Section 4.3 "O"-scope

https://user-images.githubusercontent.com/114244957/192009585-8e16aa02-4ae2-436a-bc81-8f75ac29507c.mov

The readings from the sensor are presenting fast. In order to have sufficient time to detect color change, the most current color and the color four samples away it are chosen for comparison. When there is no change in brightness, no operations are triggered. 

Remeber to release the keyboard after each press control.
```python
keyboard.release_all()
```
I found it also helpful to include a initiating time (usually 1sec) for the laptop to setup the keyboard and Adafruit9960.
```python
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
```
For this section, a ```countdown``` is used to set the operating time for this application.

### Section 4.4 RGB Reader with gesture function

https://user-images.githubusercontent.com/114244957/192053439-3e262931-612b-473b-bca0-96ef79d7c168.mov

The purpose of this function is to detect color and present its value when instructed. It can be useful when we want to detect a color of a object and record the values in a report. Four gestures are used to present, and modify the result report. 

Swiping up will ask the sensor to detect the current color and print it to a text-editable software (e.g. Texteditor, Word). Swiping down equals to backspace the line. If we want to delete the entire reading, we can swipe to the left to "undo" (command+Z) the operation. Finally, swiping to the right equals to hitting the Enter key and a new line will start.

For now, each swiping gesture will also be printed to the report so that we know that the performed gesture is valid. In future case, the printed strings can be removed to tide up the function.

### Diagram of Sec4.4 Embedded system
![WX20220923-190646](https://user-images.githubusercontent.com/114244957/192067836-b675d239-01e5-4e53-adec-18541d94554c.png)

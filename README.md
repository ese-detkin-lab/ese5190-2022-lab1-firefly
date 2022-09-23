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
The sum of the RGB is chosen even though the light of the firefly is yellow. We can also change the brightness of the LED only according to the red and green colors. However, choosing the sum of all lights can boardern the application of this sensor.

## Section 4 "'O'-SCOPE"

### Section 4.2 Change cursor's position according to the change of brightness

https://user-images.githubusercontent.com/114244957/192008665-03610ff3-35b6-4875-a315-2be82404f6b8.mov

The change of light is not stable due to the influence from the ambient light. When we change from cursor to actual "O"-scope, the performace is significently better. The code is similar to "O"-scope. It will be explained in the next section.

### Section 4.3 "O"-scope

https://user-images.githubusercontent.com/114244957/192009585-8e16aa02-4ae2-436a-bc81-8f75ac29507c.mov



### Section 4.4 RGB Reader with gesture function






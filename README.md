University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Dvisha Kishore Bakarania
        (TODO) LinkedIn, personal website, twitter, etc.
    Tested on: 

**Adafruit QT Py RP2040** and **Adafruit APDS9960 Proximity, Light, RGB, and Gesture Sensor** when come together, can help newbies create their own cool embedded system projects. Let's start! This project uses the sensor data (color, proximity, brightness) to implement a "firefly" and a custom real-time visualizer. All you will need is an Adafruit dev board with RP2040 and a sensor.

**Requirements:**

Adafruit QT Py RP2040

<img src="https://circuitpython.org/assets/images/boards/large/adafruit_qtpy_rp2040.jpg" width="200" height="200"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Plus_symbol.svg/1200px-Plus_symbol.svg.png" width="150" heigth="150"> <img src="https://cdn-shop.adafruit.com/970x728/3595-04.jpg" width="200" height="200"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Plus_symbol.svg/1200px-Plus_symbol.svg.png" width="150" heigth="150"> <img src="https://cdn1-shop.mikroe.com/img/product/wire-jumpers-female-to-female-15cm-10pcs/wire-jumpers-female-to-female-15cm-10pcs-thickbox_default-12x.jpg" width="200" heigth="200">

Now, let's implement a **firefly**!
<br />
So, the gist here is: the Neopixel led on the QT Py board should blink in synchronization with an actual firefly video. For this, we have used the brightness measurement feature of the sensor. Using the APDS9960, the brightness of the flashing firefly in the video is measured and this reading is used to control the pixels of the neopixel led by scaling the measured sensor output data to adjust the brightness/blinking of the neopixel so that it behaves just like the firefly in the video.

Below is the snippet of the code:
<br />
<br />
<img src="https://user-images.githubusercontent.com/114099174/192073633-bc447baf-d8e6-4d60-b762-73fb8102b8e6.png" width="700" height="700">
<br />
<br />
![firefly](https://user-images.githubusercontent.com/114099174/192074256-795b89fb-5ea0-4ec2-806f-01ca170b0bf9.gif)
<br />
<br />
<br />
Up-next is the implementation of a **real-time visualizer** using keyboard emulator to get real time update of the detected sensor data. This can be done using HID keyboard library. The intention here is to get a real time update of any change in brightness level as sensed by the APDS9600. 
<br />
We will be using two keys: 'O' and 'Backspace' to indicate any change at the input to the sensor. As and when there is an increase in the brightness level at the input to the sensor, any text editor in your laptop should start typing 'O's. If the brightness at the sensor input decreases then the 'Backspace' key should come into action and start erasing the 'O's so that the user is updated of the change(increase/decrease) at the sensor input. This can be done by adjusting the threshold so that an increase in brightness leads to typing 'O' and decrease leads to the erasing of 'O's using Backspace.



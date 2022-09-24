University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1
 
 Dvisha Kishore Bakarania
 <br />
 LinkedIn: [Dvisha Bakarania](https://www.linkedin.com/in/dvisha-bakarania-9370b2146?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BNtJBfZpDTEKluhukjP7uqg%3D%3D) 
 <br />
 Tested on: Windows 11 Home Version 21H2

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
<br />
![firefly](https://user-images.githubusercontent.com/114099174/192074256-795b89fb-5ea0-4ec2-806f-01ca170b0bf9.gif)
<br />
<br />
<br />
Code can also be found at: [Firefly](https://github.com/dvishab/ese5190-2022-lab1-firefly/blob/3a8a65675cf863e95c0b865e0bfb4c73537ea037/Firefly.py)
<br />
<br />
<br />
Up-next is the implementation of a **real-time visualizer** using keyboard emulator to get real time update of the detected sensor data. This can be done using HID keyboard library. The intention here is to get a real time update of any change in brightness level as sensed by the APDS9600. 
<br />
We will be using two keys: 'O' and 'Backspace' to indicate any change at the input to the sensor. As and when there is an increase in the brightness level at the input to the sensor, any text editor in your laptop should start typing 'O's. If the brightness at the sensor input decreases then the 'Backspace' key should come into action and start erasing the 'O's so that the user is updated of the change(increase/decrease) at the sensor input. This can be done by adjusting the threshold so that an increase in brightness leads to typing 'O' and decrease leads to the erasing of 'O's using Backspace.

<img src="https://user-images.githubusercontent.com/114099174/192075855-50a8592a-ec6e-4c09-8542-c984ea2ff543.png">

Also, one important point to note here is that you might probably be using a keyboard to program your RP2040, so if the RP2040 is also sending keystrokes to the 
laptop this can make it quite annoying to reprogram. So, there needs to be a way to stop it from endlessly writing the letter'O' or erasing, and that is to use an 'escape hatch'. The intention here is to make the system braek out of the main loop on sensing a partivular color. We will be using **'blue'** color. So, if I need to stop the program from endlessly writing/erasing, I should point my sensor to 'blue' color and it will break from the main loop as illustrated through the gif below:

<br />

![real_time_visualizer](https://user-images.githubusercontent.com/114099174/192076211-7a4b6884-7763-4f30-9867-19a6dc39a080.gif)
<br />
<br />
<br />
Code snippet for implementing this:

<img src="https://user-images.githubusercontent.com/114099174/192076806-79e80ac4-b325-462f-bedb-3dae83aab45d.png" width="700" height="700">

Code can also be found at: [Real Time Visualizer](https://github.com/dvishab/ese5190-2022-lab1-firefly/blob/c1ee2a235d8a2e01a7725ff37c65071b9b8b2d7a/Real_Time_Visualizer.py)




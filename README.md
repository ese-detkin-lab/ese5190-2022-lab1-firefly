University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Xingjian Chen
        (TODO) https://www.linkedin.com/in/xingjian-chen-64632b207/
    Tested on: (TODO) Lenovo R9000P (15.6-inch, 2021), Windows10

For Probelem 1, The Qt py Board we are using is not the same one as template code in the website. By using dir() command, we can find that the Qt py does not have "led" pin. It has neopixel pin, so I need to use the neopixel library and relative code to let the led on our board blink.

Same problem in problem 2, the pin on the Qt py board is different from the template code, we need to change the "SDA" and "SCL" to "SDA1" and "SCL1", then the code can run properly.

In problem 3 firefly, we can set all the RGB value in pixel.fill() command as the clear channel read by the sensor, therefore the intensity of the RGB can change with the clear value in the sensor. 

In problem 4.4, I combine the gesture sensor with the keyboard emulator. if the sensor read the gesture "UP", press A on the keyboard; if gesture "down" press B on the keyboard; if gesture "left" ,press C on the keyboard, if gesture "right"  press backspace on the keyboard. In fact, the result are very satisfying. 

Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Qiao XU
         LinkedIn:
    Tested on: Dell Inspiron 14 5410, 11th Gen Intel Core i5-113,x64-based PC
LAB1_SEC3__FireFly 

        1.the experimental result:
        
![Firefly](https://github.com/23qiaoqiaoo/ese5190-2022-lab1-firefly_Qiao/raw/main/firefly.gif)

    The build-in LED brightness of RP2040 will change synchronously according to the external brightness detected by the APDS9960.
    
        2.Gain: 
    I learned how to convert the brightness value of external light(which is 0-65535 for APDS9960) to the light value that is used to control the brightness of build-in LED in the RP2040. A higher value means a higher light density.

LAB1_SEC4.4

        1.Overview: 
    In this project, I used the gesture sensor and the color sensor in the APDS 9960 to control the LED light in the RP2040 and the arrow movement on my computer.
    
    1)Gesture sensor:
    "Up" and "Down" gesture are used to control the movement of the arrow. If the gesture is "UP", then the arrow go up for one line, if the gesture shows "Down", then the arrow goes down for one line. 
    
![Up_Down](https://github.com/23qiaoqiaoo/ese5190-2022-lab1-firefly_Qiao/raw/595e70c546ee0b2c20d5ae1cc58aa1b2f03dff7a/Up_Down.gif)
    
    "Left" and "Right" gesture are used to control the beginning and the end of the light show. When gesture is detected to be "Left", the keyboard function will be used to print the spring--"rainbow light show!^_^", and then after 4 seconds, the rainbow light, which is made of 7 different colors, will be displayed and then stayed white(the last color displayed) until the "Right" gesture is detected. If the "Right" gesture is detected, the "keyboard_layout.write" will be triggered to display ""The show is end, Thanks>~<!", and the LED light will be turned off at the same time.

![Left_Right_gesture](https://github.com/23qiaoqiaoo/ese5190-2022-lab1-firefly_Qiao/raw/595e70c546ee0b2c20d5ae1cc58aa1b2f03dff7a/Left_Right_gesture.gif) 
    
    2)color sensor
    The color sensor is used to detect the external brightness and change the brightness of the rainbow light show correspondingly.
    
![Color_control](https://github.com/23qiaoqiaoo/ese5190-2022-lab1-firefly_Qiao/raw/6d34310b3f8e910ca982e1fc4f8acae3dbef5447/Color_control.gif)

        2.Diagram:
![diagram](https://github.com/23qiaoqiaoo/ese5190-2022-lab1-firefly_Qiao/blob/e96f87ea3d92e6aa9706ec7b72d23964c429222e/diagram.jpg)    

        3.Result:
     1) for rainbow light control:
![4.4_light_control](https://github.com/23qiaoqiaoo/ese5190-2022-lab1-firefly_Qiao/blob/bed58742ed3d488aa72477110a7950b255d9995f/4.4_light_control.gif)

    2) for arrow control
![4.4_mouse arrow move](https://github.com/23qiaoqiaoo/ese5190-2022-lab1-firefly_Qiao/blob/bed58742ed3d488aa72477110a7950b255d9995f/4.4_mouse%20arrow%20move.gif)
  



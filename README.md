University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Yuchen Wang
        wangyuchen0303@gmail.com
    Tested on: MacBook Pro (14-inch, 2021), macOS Monterey 12.6

Lab#1 Submission:

Part3:

3.2 Firefly Video

![IMG_9329](https://user-images.githubusercontent.com/105755054/192004338-217a584d-7f3a-4f73-877c-03b3e5def980.GIF)

In this part the 'color_integration_time' has benn set to 40, and the value of the clear channel is choosed to the indicator of Neopixel LED, and within this code 'r = g = b = clear' since we only pay attention to the LED dims and brights.
    
Part4:

4.2 Moving cursor with the brightness changing

![IMG_9331](https://user-images.githubusercontent.com/105755054/192006781-740d8b2c-ab0e-4124-9f22-f8ff2a2ca1ac.GIF)

The Cursor will move with the brightness changing, and the value of color_integration_time is set as defult of 255. Additionally, the thresholds of the clear is 400.
 
4.3 "O" - SCOPE Video

![IMG_9333](https://user-images.githubusercontent.com/105755054/192009163-2ffd2810-7859-4c7c-9d18-a0c00a728716.GIF)
    
In this part, the color_integration_time has been set to 10 for more sensitive. To be more spcific, for comparing the differences between the brightness, I called the function called 'get_brightness' twice and a 0.1s delay between them to get the brightness differences.
    
4.4 Personal Project
    
GIF of 4.4:

![IMG_9335 2](https://user-images.githubusercontent.com/105755054/192013009-bfd20d66-d545-4baf-994e-764f7ee7bb20.GIF)
    
Overview of 4.4:

In lab 4.4, I used the Adafruit 2040 and ADPS9960 sensor to control the playback or go forward of YouTube videos,such as fast-forwarding 15 seconds and increasing or decreasing the volume 15% of playing video. Since the YouTube video website can use the arrow keys on the computer keyboard to control the video. Like, the left arrow keys and right arrow keys are used to control the fast forward and backward 5 seconds respectively; the up and down arrow keys of the keyboard can control the volume of the video playback. Thus, all I had to do was press the arrow key when the sensor detected a certain hand movement above it, such as a hand wave to the Right, and the sensor sensed it and returned a str "Right", then used "keycode.RIGHT_ARROW" to control the computer and virtually press the Right arrow to make the playback of the YouTube video. I will use a flow chart to show the specific control details. Because nearly all video player compatible with the four directions arrows of keyboard, then it can widely use in many players. Additionally, users do not have to press any bottoms, which means it is more user-friendly for disabled people.
    

Here is the Float Chart for explaining more detail:

![FloatChart4_4](https://user-images.githubusercontent.com/105755054/192039993-94391ba0-0046-45c9-8cd7-87c0b172d8fa.png)
    
System Diagram:

Here is the Diagram of this part:

![Lab4_4Diagram](https://user-images.githubusercontent.com/105755054/192035710-e6fdf036-e08a-452d-b3cd-f9422a85af93.png)
    
    


    
    

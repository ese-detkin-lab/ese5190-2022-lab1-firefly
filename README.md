University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    (TODO) Name: Michael Peters
        (TODO) mvpeters@seas.upenn.edu
    Tested on: (TODO) Microsoft Surface Laptop (13.5-inch, 2017), Windows 10 Pro

(TODO: Your README)

Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.).

My Gifs for part 3 and part 4 are attached in the repo, I'm wasn't able to figure out how to link them to this post.

Part 4.4 Visualizer Overview

For my part 4.4 I used the proximity sensor to create a simple system that reads the distance of an object and then lights up an LED and displays a message based on that reading. This used both the proximity and color reading features of the APDS. For the LED, when your hand is close to the object and ambient light is being blocked out the LED dims. When your hand is further away the brightness increases. For the distance reading, if the object is getting closer it prints “Object Closer” and if it is moving away it prints “Object Further”. This was done just using a simple if loop that compares the current reading to the reading from the last iteration.

This simple system could be used to represent how an autonomous car might work. Depending on the distance it picks up from an ultrasonic sensor it could vary the speed using the reading or display a message if an object is approaching. In my code the LED brightness was still based on the color reading because I wanted to use both, but it could be easily changed to be based on the distance. If it was designed to turn on when an object is too close then that could perhaps represent brake lights.

![image](https://user-images.githubusercontent.com/114199773/192070349-5a5aadcc-c1f3-4e59-9714-6d12884a1a55.png)


The user varies the distance of the object, which in the gif attached was my hand. The APDS then reads that distance and outputs that information to the RP2040. The RP2040 varies an LEDs brightness depending on the distance and then stores that distance value. After another value is received from the APDS, the RP2040 compares it and tells the PC to print a message of whether the object is getting closer or further away. If the distance stays the same then no message is output. 

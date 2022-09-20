University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    (TODO) Meiyi Yu
        (TODO) https://www.linkedin.com/in/meiyiyu-thea/
    Tested on: (TODO) MacBook Pro (13-inch, 2019), macOS Monterey 12.3.1

(TODO: Your README)


Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

## 3.2 Firefly:

![](firefly.gif)


## 4.4 keyboard lib play around

![](4.gif)

Overview for 4.4

I setted up four events for the keyboard activities:

    i. if the color detected is red (r > 250), press key 'r'
    
    ii. if the color detected is green (g > 80), press key 'g'
    
    iii. if not the above two cases, press backspace
    
    iv. if it is dark (c < 10), break
    
The sensor detected data is quite unstable, also the light color depends a lot on the environment and transmission delay, so I adjusted the thredshod(e.g. 250, 80, 10) under my apartment environment and set the Time Register Cycle as 256 to present better visualization.
At first I also considered using gesture sensor and distance sensor, but the effect is not that good. The distance would conflict with the color detection, and the gesture sensor is not that sensitive. So at last I settled down for only enable color sensing.

4.4 diagram:

<img width="809" alt="image" src="https://user-images.githubusercontent.com/84453030/191382649-ee17791f-f8f0-4f3d-bf7e-466d1551e34c.png">




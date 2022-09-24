University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Maxi Liu
         
    Tested on:  MacBook Pro (13-inch, 2017), macOS Monterey 12.5.1


For section 3.2, I set the light blink according to the firefly:

while True:
    r, g, b, c = sensor.color_data
    if(c >= Last + 200):
        pixels.fill((255, 255, 255))
    else:
        pixels.fill((0, 0, 0))
    Last = c
    time.sleep(0.02)
    
So when the brightness is higher, the LED would blink.
This is the GIF for demonstration:
![Alt text](firefly.gif) 

For my 4.4 section I make a light detector, which means the keyboard will print relative messages according to the brightness. 
In the code, I set different keys for the keyboard:
key="So dark! I am so scare!!!\n"
key1 =  "dim!\n"
key2="lighter now!\n"
key3="My eyes!!!My eyes!!!!?\n"


So in the while loop I will make the chip detect the brightness, and keyboard will type messages according to the brightness(for example, "So dark! I am so scare" when brightness is very low). 
This is the demonstration:
![Alt text](section4_4.gif)

To deconstrate the connection between APDS9960, RPS2040, laptop and me, I drawed a picture to demonstrate:
<img width="769" alt="image" src="https://user-images.githubusercontent.com/58932929/192072873-c08992a2-b1d2-4325-8182-dde4e1ec49b4.png">

First the laptop send the code to RP2040 and RP2040 process and give the direction to the APDS9960. APDS9960 would use the sensor and send the gathering information(brightness), and I have the control to make it gather the ceration information(brighter or dimmer), to the RP2040, so that RP2040 can react to the information according to the code. 

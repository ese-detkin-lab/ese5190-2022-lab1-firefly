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



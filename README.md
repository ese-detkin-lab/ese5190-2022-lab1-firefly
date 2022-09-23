University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

Essa Alkhunayn ,partner with Amogh and Saurabh.
http://linkedin.com/in/eng-essa-alkhunayn-pmp%C2%AE-21327b14b.
Tested on Lenovo Laptop-DN757U7U  (15-inch, 2021), Microsoft Windows 10 Home-64bit


PART 1: MICROCONTROLLER 

1.1 installing CircuitPython 7.x on RB2040.

![Circuitpaython](https://user-images.githubusercontent.com/114237225/192063592-dfd6e34b-247d-4772-b0fe-de12db88e468.jpg)


1.2 Blinking LED program.

![WhatsApp Video 2022-09-23 at 8 51 43 PM](https://user-images.githubusercontent.com/114237225/192063858-389171dd-01cf-451c-aa8e-928630b7513e.gif)


1.3 cummuncate throgh REPL-serial console.

![REPL](https://user-images.githubusercontent.com/114237225/192064036-d5b14066-02fa-4235-b260-067b04d3b579.png)


Part 2:

Python Installation of APDS9960 Library.
Proximity Reading
Color Reading.
Gesture Reading.


Part 3: FIREFLY simulator.

In the Firefly simulator, we used a color sensor (APDS9960) to detect the brightness of the incoming light (Firefly video) and set a threshold at which the system switches the LED ON in RP2040. 

![WhatsApp Video 2022-09-23 at 9 58 06 PM](https://user-images.githubusercontent.com/114237225/192064457-d82d21c1-523b-4e11-84b8-714990a89e42.gif)

![WhatsApp Video 2022-09-23 at 10 12 25 PM (1)](https://user-images.githubusercontent.com/114237225/192065415-8ed22538-eae1-4f04-92f2-651e9be6f5ec.gif)


Part 4: Real time Visualizer.

For the Keyboard visualizer, we have used the NotePad with the character 'O' indicating the brightness level of the object with changing light intensity.  In the algorithm, previous brightness values are saved and compared with the current values in the next iteration of the loop. If the current brightness is greater than the previous brightness, 'O' is printed once, and if the current brightness is less than the previous brightness, the backspace is pressed once. 

![WhatsApp Video 2022-09-23 at 9 49 45 PM](https://user-images.githubusercontent.com/114237225/192064765-8cf792cb-4069-47ce-b261-b3775a1d7724.gif)

![WhatsApp Video 2022-09-23 at 10 22 24 PM](https://user-images.githubusercontent.com/114237225/192064781-43305575-c156-4b92-a9dc-e73ffda29e08.gif)



![diagram of real-time visualizer](https://user-images.githubusercontent.com/114237225/192065487-9bcbefb3-d702-4c15-9e45-a15e35824164.jpg)


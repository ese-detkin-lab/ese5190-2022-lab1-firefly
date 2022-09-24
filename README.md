University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Name: Prateek Bashista
    Linkedin: https://www.linkedin.com/in/prateek-bashista-27858216a/
    Tested on:  HP Pavillion Gaming (15.6-inch, 2020), Windows 11

Exercise 3.2
To implement the Firefly functionality using the Brightness index of Color Sensor 

The functionality is implemented in following:
1) The color sensor is evoked and data is read from it. There are 4 channels of data available from the onboard color sensor. They are 'r', 'g' , 'b' and 'c'. The brightness reading is given in 'c'. 
2) The vaue of c ranges from 0 to 65535. This is too large for the pixel range. so , we map the entire range of c over 255 unique values. This value will be used to control the brightness of the led. Following formula is used: 
                                        p = (c/65535)*255
3) The 'p' variable is used as function argument of pixel.fill(arg,arg,arg) function.
4) The readings of c is read in the environment and threshold on when to switch on the led is taken. 
5) If the value of sensor is greater than threshold, led is switch on other off.
Note: Delay is given before the start of the loop so that , keyboard does not start immediately printing on the code itself




![6ui0kc](https://user-images.githubusercontent.com/23244847/192072546-bd10a614-ab46-4ffb-a40a-69ce3d11e5ca.gif)




Exercise 4.4
This functionality is build by incorporating the features of keyboard hid library and the color sensor reading of brightness. The output data of the sensor is between 0 and 65535. This is not in pure readable format for the end user. So, we compartmentlised the data into different ranges , with each range having its keyword. So, the levels are {Dim, Bright, Brighter, Brightest, Burnt Retinas}. In this fucntionality, as the torch comes closer to the sensor, more light it detects, and highrer the reading it gives. 
Following is the Implementation:
1) The value of 'c' from the color sensor is read. 
2) "If" conditions are used to test, which range the value lies in.
3) The value of c is mapped on the range of 0:255. Ths enables us to control intensity on-board led as the light source moves closer, the led burns brightly.
4) The message is printed using keyboard hid library based on the range value lies in. 


![alt text](https://github.com/prateekbashista/ese5190-2022-lab1-firefly/blob/af1bcd53eb6120af14c140063eb2b53dcf6f92ab/4.4%20diagram.png)

![6ui10p](https://user-images.githubusercontent.com/23244847/192072772-a9eca0bd-1056-4816-8980-1459cda44721.gif)


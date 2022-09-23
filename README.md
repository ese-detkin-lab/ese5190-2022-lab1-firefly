University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Name: Prateek Bashista
    Linkedin: https://www.linkedin.com/in/prateek-bashista-27858216a/
    Tested on:  HP Pavillion Gaming (15.6-inch, 2020), Windows 11

Exercise 3.2
To implement the Firefly functionality using the Brightness  index of Color Sensor 

The functionality is implemented in following:
1) The color sensor is evoked and data is read from it. There are 4 channels of data available from the onboard color sensor. They are 'r', 'g' , 'b' and 'c'. The brightness reading is given in 'c'. 
2) The vaue of c ranges from 0 to 65535. This is too large for the pixel range. so , we map the entire range of c over 255 unique values. This value will be used to control the brightness of the led. Following formula is used: 
                                        p = (c/65535)*255
3) The 'p' variabe is used as function argument of pixel.fill(arg,arg,arg) function.

insert gif////////////////////////////////////////////////////

Exercise 4.4

Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

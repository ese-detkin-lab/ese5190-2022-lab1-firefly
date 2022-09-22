University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Saurabh Sandeep Parulekar
       LinkedIn: https://www.linkedin.com/in/saurabh-parulekar/
    Tested on: HP Pavillion Gaming Laptop, Windows 10 21H2



## Firefly Visualizer

![](https://github.com/amoghgajare/LAB1-AMOGH-GAJARE-WORKED-WITH-SAURABH-PARULEKAR/blob/main/firefly.gif)

In the firefly visualizer, we have used the color sensor on APDS9960 to detect the brightness of the incoming light (firefly video in our case) and set a threshold above which the system will toggle the LED on RP2040 ON. The threshold, to make it a good fit for all lighting conditions, instead of providing a test case-specific threshold, we use the moving average method on 200 initial samples to set the threshold in the code itself. 


## Custom Visualizer

![](https://github.com/amoghgajare/LAB1-AMOGH-GAJARE-WORKED-WITH-SAURABH-PARULEKAR/blob/main/real-time-visualizer.gif)

For the custom visualizer, we have used the NotePad with the character 'O' indicating the brightness level of the object with changing light intensity. The brightness is in the range of 0 to 65535, we have normalised it to 0 to 50. In the algorithm, previous brightness values are saved and compared with the current values in the next iteration of the loop. If the current brightness is greater than previous brightness, 'O' is printed once, and if current brightness is less than previous brightness, backspace is pressed once. By this, relative brightness is measured instead of absolute value. For testing we have used the firefly video. For fail-safe operation, the brightness needs to be zero to begin the execution of the code. in Mouse cursor control, the cursor is horizontally moved to the relative right for increasing brightness, and relatively to the left for decreasing brightness.

![](https://github.com/amoghgajare/LAB1-AMOGH-GAJARE-WORKED-WITH-SAURABH-PARULEKAR/blob/main/diag.jpg)

Figure above is the Design of the system implementing the Custom Visualizer

# Part 3:
In part 3, we use APDS9960 to detect color and display the detection results on RP2040. 
We enable the color detection function on APDS9960 and store the data in r, g, b and c, which represent red, green, blue and clear data detected by APDS9960’s sensor respectively.
To display APDS9960’s sensor readings in real time, we have to change the number of samples for each sensor reading. In APDS9960’s data sheet, it shows that the value of color_integration_time determines time between readings. The default value is 256 and we could set this value small to speed up the sensor readings.


![screenshot1](https://user-images.githubusercontent.com/113371324/191817230-a68f800b-3ca7-4bbf-b15f-7f5a999350a6.png)

![screenshot2](https://user-images.githubusercontent.com/113371324/191817294-d1a07b96-58b6-4834-9639-6d7152f0cb81.png)
![screenshot3](https://user-images.githubusercontent.com/113371324/191817331-54c98fd4-b16e-46f1-842a-02392a846df0.png)

The display result is shown below:

![4_4record_AdobeExpress](https://user-images.githubusercontent.com/113371324/191828183-40272fe2-ccc7-48b0-aeb1-79829e2eb0b7.gif)

Clearer gifs are in the gif folder

# Part 4:
In part 4, we visualize APDS9960’s brightness reading by sending keyboard output and displaying them on the laptop. The sensor reads brightness twice in a very short time and the data are saved in different variables. By comparing these variables, the controller knows whether the environment is getting brighter or darker. And when the brightness increases, the keyboard will output "Crazy Thursday !!!", press the "RETURN" key and the green LED on RP2040 blinks, while the brightness decreases, the keyboard will output "V me 50", press the "RETURN" key and the blue LED on RP2040 blinks. To break the program, an 'escape hatch' is settled as if the light intensity is too low, the code stops running.

The display result is shown below:

![4 4 (1)](https://user-images.githubusercontent.com/113371324/191993379-b513ab70-975d-4c20-a816-60d49bcee2ae.gif)




Clearer gifs are in the gif folder


diagram that showws how the components interact is showing below:

The![111](https://user-images.githubusercontent.com/113371324/191833299-10c01f1e-5b94-4646-b18b-c7938de7c449.jpg)



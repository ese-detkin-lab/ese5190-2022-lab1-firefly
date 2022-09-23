University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1


    Xiayu Zeng
        xiayu027@seas.upenn.edu
    Tested on: MacBook Air (13-inch, 2020), macOS Monterey 12.5


# Part 3:
In part 3, we use APDS9960 to detect color and display the detection results on RP2040. 
We enable the color detection function on APDS9960 and store the data in r, g, b and c, which represent red, green, blue and clear data detected by APDS9960’s sensor respectively.
To display APDS9960’s sensor readings in real time, we have to change the number of samples for each sensor reading. In APDS9960’s data sheet, it shows that the value of color_integration_time determines time between readings. The default value is 256 and we could set this value small to speed up the sensor readings.

The display result is shown below:
![2761663946358_ pic](https://user-images.githubusercontent.com/114005477/191995779-3e05feb6-b506-46e7-8705-3ddcdea9143b.jpg)
![2771663946369_ pic](https://user-images.githubusercontent.com/114005477/191995786-0c9df5b2-00b4-4149-865f-601acd85bcba.jpg)
![2781663946390_ pic](https://user-images.githubusercontent.com/114005477/191995797-ccf0d3cd-4d98-4c25-baf0-0afacb915b20.jpg)

# Part 4:
In part 4, we visualize APDS9960’s brightness reading by sending keyboard output and displaying them on the laptop. The sensor reads brightness twice in a very short time and the data are saved in different variables. By comparing these variables, the controller knows whether the environment is getting brighter or darker. And when the brightness increases, the keyboard will output "Crazy Thursday !!!", press the "RETURN" key and the green LED on RP2040 blinks, while the brightness decreases, the keyboard will output "V me 50", press the "RETURN" key and the blue LED on RP2040 blinks. To break the program, an 'escape hatch' is settled as if the light intensity is too low, the code stops running.

The display result is shown below:


The diagram that showws how the components interact is showing below:
![2301663874311_ pic_hd](https://user-images.githubusercontent.com/114005477/191832837-7452cb1f-a5ce-4ee2-abfd-c0f32500f5a5.jpg)

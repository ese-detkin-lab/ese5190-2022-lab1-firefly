University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

(TODO) SUSHRUT THAKUR
   
Tested on: (TODO) Lenovo Legion 5 AMD Ryzen 7 (15-inch, 2022), Windows 11

Lab 1: Sushrut Salil Thakur worked with Juilee Samir Kotnis 
# ESE-5190-lab

Proximity - 

The components used for this experiment are RP2040 microcontroller and APDS9960 sensor board. The aim of this experiment was to print the proximity being sensed by the APDS9960 sensor board on our monitor. With respect to the attached GIF, it can be seen that the APDS9960 sensor board measures the distance of the hand from the sensor with 8 bit resolution. When the hand is very close to the sensor, proximity reading is observed to be 255 which is the maximum ADC count. As the hand moves away from the sensor, the proximity reading decreases.

![](https://github.com/sushrut-upenn/ESE-5190-lab/blob/main/proximity.gif)


Firefly - 

The components used for this experiment are RP2040 microcontroller and APDS9960 sensor board. The aim of this experiment was to turn on the LED on RP2040 when the APDS9960 color sensor senses bright light and turn off the LED when there is no bright light falling on the LED thus enabling the blinking of the LED. With respect to the attached video and GIF, it can be seen that the Color and ALS detection feature of RP2040 provides data regarding Red, Blue, Green and Clear light intensity. We set a threshold value for the clear light and when the light source was flashed at the sensor, the serial monitor printed the data for Red, Blue, Green and Clear light and the LED on RP2040 turned on. When the light source was dimmed and could not cross the threshold, the monitor printed data for Red , Blue, Green and Clear light which were lesser than the previously printed values thus showing a difference in the intensity and the LED on RP2040 was also turned off. This behavior of the LED mimics the behavior of a Firefly.

![](https://github.com/sushrut-upenn/ESE-5190-lab/blob/main/Firefly.gif)


Keyboard Emulator - 

Block Diagram - 

![block-diagram](https://user-images.githubusercontent.com/114092860/191882940-b96a4859-c132-4d38-90e3-56a1ad335f10.png)


The components used for this experiment are RP2040 microcontroller and APDS9960 sensor board. The aim of the experiment was to print a character ‘O’ and backspacing it using RP2040 which emulates a keyboard. With respect to the attached video and GIF, it can be seen that when light is flashed at the APDS9960 sensor, the RP2040 starts typing the character ‘O’ on any document that is kept open and when the light source being flashed at the APDS9960 is dimmed, the RP2040 starts backspacing the data that was previously typed. This is done using the HID keyboard library that helps RP2040 emulate a keyboard.

![](https://github.com/sushrut-upenn/ESE-5190-lab/blob/main/emulator.gif)


Lab 1: Juilee Samir Kotnis Worked with: Sushrut Salil Thakur

(TODO) Juilee Samir Kotnis
Tested on: (TODO) Legion 5 (15.6-inch, 2020), Windows 11

# ESE-5190-Lab-1
![](https://github.com/JuiUpenn11/ESE-5190-Lab-1/blob/main/short-proximity.gif)

Explanation for Proximity:
The components used for this experiment are RP2040 microcontroller and APDS9960 sensor board. The aim of this experiment was to print the proximity being sensed by the APDS9960 sensor board on our monitor. With respect to the attached GIF, it can be seen that the APDS9960 sensor board measures the distance of the hand from the sensor with 8 bit resolution. When the hand is very close to the sensor, proximity reading is observed to be 255 which is the maximum ADC count. As the hand moves away from the sensor, the proximity reading decreases.

![](https://github.com/JuiUpenn11/ESE-5190-Lab-1/blob/main/short-firefly.gif)

Explanation for Firefly:
The components used for this experiment are RP2040 microcontroller and APDS9960 sensor board. The aim of this experiment was to turn on the LED on RP2040 when the APDS9960 color sensor senses bright light and turn off the LED when there is no bright light falling on the LED thus enabling the blinking of the LED. With respect to the attached GIF, it can be seen that the Color and ALS detection feature of RP2040 provides data regarding Red, Blue, Green and Clear light intensity. We set a threshold value for the clear light and when the light source was flashed at the sensor, the serial monitor printed the data for Red, Blue, Green and Clear light and the LED on RP2040 turned on. When the light source was dimmed and could not cross the threshold, the monitor printed data for Red , Blue, Green and Clear light which were lesser than the previously printed values thus showing a difference in the intensity and the LED on RP2040 was also turned off. This behavior of the LED mimics the behavior of a Firefly.

![Block Diagram](https://user-images.githubusercontent.com/114092868/191881937-78bb240b-406c-41c2-91f9-fbe21f23bd58.png)
Explanation for Keyboard Emulator:
The components used for this experiment are RP2040 microcontroller and APDS9960 sensor board. The aim of the experiment was to print a character ‘O’ and backspacing it using RP2040 which emulates a keyboard. With respect to the attached GIF, it can be seen that when light is flashed at the APDS9960 sensor, the RP2040 starts typing the character ‘O’ on any document that is kept open and when the light source being flashed at the APDS9960 is dimmed, the RP2040 starts backspacing the data that was previously typed. This is done using the HID keyboard library that helps RP2040 emulate a keyboard.

![](https://github.com/JuiUpenn11/ESE-5190-Lab-1/blob/main/short-emulator.gif)



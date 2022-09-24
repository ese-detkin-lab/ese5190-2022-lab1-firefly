University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    NAVIT GILL
       
    Tested on: MacBook Pro (13-inch 2018), macOS Monterey 12.6

# ESE5190-Lab1Firefly
ESE5190 Lab 1 repository - Navit Gill

# Sec 3.2 Firefly Video
Used APDS9960 sensor to sense the brightness. Used "clear" channel from color sensor.
if c (clear) > 100 LED on RP 2040 was bright (brightness 255)
else LED was dim (brightness 5)
Working example showed in video https://github.com/navgill4/ESE5190-Lab1Firefly/blob/main/lab1_sec_3_2_compressed.mp4

# Sec 4.4 Custom Visualizer
Created the custom visualizer for lab 1 section 4.4 using the keyboard hid library.
Used the gesture reading from the APDS9960 sensor and mapped each letter of the english alphabet and 'space' and 'backspace' to a gesture/set of gestures https://github.com/navgill4/ESE5190-Lab1Firefly/blob/main/custom_visualizer_logic.jpeg
wrote my first name (navit) on a text editor on my computer using the gesture map and keyboard hid as shown in the video https://github.com/navgill4/ESE5190-Lab1Firefly/blob/main/lab1_sec_4_4_compressed.mp4
User swipes finger over the APDS9960. It records the gesture based on the direction of the swipe. APDS9960 sends gesture info to the microcontroller using I2C. RP2040 uses the keyboard HID library to control the keyboard on the PC. PC displays the text based on the gesture info to the user on a text editor/similar app on the PC. https://github.com/navgill4/ESE5190-Lab1Firefly/blob/main/interaction_diagram.jpeg

University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Arnav Gadre
        linkedin.com/in/arnav-gadre-b261491a3
    Tested on: DELL Inspiron 7400 (Intel i7 11th Gen), Windows 11 (64-bit)

## Firefly
- We take color readings in the form of r, g, b, and clear; using the APDS 9960. 
- These values are passed to the RP 2040 board, after scaling down.
- Depending on the intensity of te light from the Firefly video, the r, g, b and c values keep changing in real time, which is visible on the MU editor. 
- The LED on RP 2040 replicates the light from the video, and changes the brightness of the LED in real-time.

![](/Media/Arnav_Gadre_Firefly.gif)

## Keyboard Emulator

- Here, we are using the RP 2040 to replicate a keyboard.
- We are again taking the brightness data as an input on the APDS 9960, and feeding it to the RP 2040. 
- When the nrightness is low, the letter 'a' is being printed on the Word file. When the brightness is high (after exposing the APDS 9960 to the phone flashlight), we call the backspace function, so the typed letters get deleted.
- All these changes are happening in real-time, as is evident from the video.

![](/Media/Arnav_Gadre_Keyboard_Emualtor.gif)

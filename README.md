University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Shu Xu
        Lab 1 submission
    Tested on: Windows 10

    This lab was compeleted late since this student has not obtained the
    lab equipment until the due date (Sep 23rd). The new hard due date is
    set to be Sep 30th.

Overview for custom visualizer from 4.4

    In part 4.4, a Morse code Decoder is constructed by reading the gesture
    movement right/left/up/down as dot/dash/enter/backspace. Then the
    corresponding letter/action key will be pressed on PC keyboard. The
    link to a GIF that shows the performance of this system is given
    here: [Part4.GIF](https://github.com/shux3/ese5190-2022-lab1-firefly/blob/main/part4.GIF)
    
    In this system, a dictionary of morse code, named 'Morse_dict' is used
    to select the letters based on input gestures. A str variable named
    'code' is used to store the input dots/dashes, which will be cleared
    once the enter/backspace action is triggered.
    
    The diagram of this embedded system is shown as below:
![System_diagram](https://user-images.githubusercontent.com/50347795/192923299-a71ab54e-09ba-421b-8695-55e3a2cb34c7.jpg)


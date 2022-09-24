University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

(TODO) Name: Chongyuan Zhang

(TODO) Email: zcy6@seas.upenn.edu

Tested on: (TODO) Lenovo Legion (R9000X), windows 11

(TODO: Your README)
Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

---

### Part 3:
#### 3.2 firefly visualizer
Overview:
The brightness of the LED of RP2040 will change based on the 'clear' value of the APDS9960's brightness reading.

![5c0be2d062261195686d1d5cb631cdbd](https://user-images.githubusercontent.com/114255407/192070779-91574322-6bba-472a-aecc-d55b71ee5a24.gif)



### Part 4:
#### 4.2 Mouse cursor moving horizontally based on the APDS9960's latest brightness reading
Overview:
Mouse cursor will move to the left in strong light, and will move to right in the dark. In the natural environment, mouse cursor does not move.

![c8ff7edb94fa2a0d9bdd6cb299f7566c](https://user-images.githubusercontent.com/114255407/192070838-a9bff96e-85b6-429e-9dee-ea1918d3adf6.gif)


#### 4.3 "O" & "backspace" input based on the brightness reading
Overview:
I have set comparing loop of the clear value of the brightness, when the 'clear' value of the brightness is increasing, the computer will type the letter "O" autometically. When the 'clear' value of the brightness is decreasing, the computer will send the "backspace" autometically. If the 'clear' value of the brightness didn't change, there is no any commands sent (For example, keeping the sensor in the dark)

![e16c685bdb5027be90cc968b5023cf5b](https://user-images.githubusercontent.com/114255407/192070488-df6b0901-943a-4860-aa60-73cccc497fe1.gif)

#### 4.4 Custom real-time visualizer
Overview:
In this section, I accomplished send "UP_ARROW","DOWN_ARROW","LEFT_ARROW","RIGHT_ARROW" commands via gesture of "up", "down", "left", "right" individually based on the APDS9960's gesture reading.

![d3212c02e61851b6905e88a33b82f60e](https://user-images.githubusercontent.com/114255407/192070502-0d83f93f-fecb-4706-bdd6-1acc7ec7641b.gif)




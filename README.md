## University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Yixuan Wang
        https://www.instagram.com/shericlare/
    Tested on: ASUS TUF Gaming F15, Windows 11

### 3.2 Firefly 

- **Requirement**: Load the video of an actual firefly closely in front of the sensor, and record how the led the RP2040 flashes(if it is in sync with the firefly).

- **Analysis**: We need to track the brightness and adjust the output parameter of the led.

**[firefly.gif](https://github.com/Sharonun/ese5190-2022-lab1-firefly/blob/main/3.2.gif)**
 
### 4.4 Custom real-time visualizer

- **Requirement**: Send some keyboard commands to a text display on the laptop. And the display should 
update in “real time” along with the sensor.

- **Function of my system**: To express my deep **love** to Upenn(?)

- **Rules**:

1. When the system runs, where will be a "I L" display on the screen.

2. When the brightness increases(or with no significant decline),the RP2040 will keep typing the letter"o".

3. When the brightness decreases(e.g. the value of "c" changes more than 200), the RP2040 will keep sending a ‘backspace’ command.

4. When the sensor is coverd by sth, the RP2040 will stop running and type"ve Upenn".


Then we will see sth like this:(I am just trying to make it longer)

<img width="709" alt="image" src="https://user-images.githubusercontent.com/114169032/191848795-94b733ff-453d-4ec9-83ff-6d534c5e4911.png">

**[4.4gif](https://github.com/Sharonun/ese5190-2022-lab1-firefly/blob/main/4.4.GIF)**

- Here's a diagram:
![diagram](https://user-images.githubusercontent.com/114169032/191854762-4aab0df6-5c94-432d-8e0f-34c2f679c1ea.png)

**But there do exist a problem: I don't know how to retpye in "I" and "L"after they are removed by "backspace" command.**




University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Yuan Chi
    https://github.com/ChiYuan9
    Tested on: MacBook Air (13-inch, 2019), macOS Monterey 12.5.1

# Overview of Project 4.4

This project is like an interactive game. And the mission of this game is to change the brightness variation trend received by the sensor for 6 times.

Step 1, RP 2040 will type:“Game Start！Mission: Changes the brightness variation trend received by the sensor for 6 times.”on the screen.

Step 2, RP 2040 will type: “Now, Get Brighter!” on your screen, that means you need to let the sensor receive a brighter light. If you accomplish that requirement, RP 2040 will type: “Done” on your screen and the LED connected to RP 2040 will also shine a white light.

Step 3, RP 2040 will type: “Now, Get Darker!” on your screen, that means you need to let the sensor receive a darker light. If you accomplish that requirement, RP 2040 will type: “Done” on your screen and the LED connected to RP 2040 will also shine a white light.

Following the instruction typed on the screen, you need to cycle step 2 and step 3 for two more times to complete the mission. After you complete the mission, RP2040 will type “Mission Success!” on the screen, and the LED will shine a green light. The program end.

If you want to stop the game, just cover the sensor with your hand, and RP2040 will type “Game Interrupted, Mission failed!” on the screen, and the LED will shine a red light. The program end.

# University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

Yangbo Zhou
Tested on: HP Envy 13, Windows 11

# Part 3.2
![part3 2](https://user-images.githubusercontent.com/90922933/192077534-5483029a-3911-4d0f-9949-9c06b7c9e016.gif)

# Part 4.4
![part4 4](https://user-images.githubusercontent.com/90922933/192077544-26ddfea2-1444-423b-83c3-abd5957dd498.gif)

# Objective
For part 4.4, our idea is using the interaction between users and the gesture sensor to control the cursor and keyboard.
In this casing, we create a matrix full of zero, except only a 1 inside. The users can use their gestures to control the curser to move up, down, left and right. (The cursor is not that obvious in the gif.) After you moved the cursor to the target position, push your hand to the sensor twice as a double click. Then the code will delete the 1 and replace it with a 0. Congratulations! Your matrix is fixed! :)

# Diagram
![1663990535(1)](https://user-images.githubusercontent.com/90922933/192078399-95cc3f85-57c4-4b3d-9a37-c1551230b075.png)

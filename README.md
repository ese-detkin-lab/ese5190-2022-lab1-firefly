University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    (TODO) Zhuoling Li      Worked with Yixuan Wnag
        (TODO) Zhuoling@seas.upenn.edu
    Tested on: (TODO) MacBook Pro (14-inch, 2021), macOS Monterey 12.5.1

(TODO: Your README)

Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

Sec.3.2 Firefly

![3 2](https://user-images.githubusercontent.com/114199800/191886242-a2c408a7-3b44-4247-bac5-367f02aa8b29.GIF)

Sec.4.4 Customized visualizer
In the design, I choose to use the APDS9960 to detect the changes in light and then changes it into signal transe to the RP2040, the program in RP2040 will control the keyboard to type in the keyboard. More specificaly, when the brightness increase one time, the program will simulate to type "Brighter" one time in the editor. If the brightness decrease one time, the program will simulate to type "Darker" one timein the editor. When the light can't be detected, the program will simulate to type "System Off" in the editor, and the system will stop working at the same time.
As shown Below

![Sec4 4](https://user-images.githubusercontent.com/114199800/191886944-503508bb-3505-40a3-a713-762d4b7319a7.GIF)

In the desin, In order to make the system work better and be less affected by the environment, I set the integration time to 60, and according to my environment, set the basic ambient light intensity to 150. At the same time, according to the actual measurement, set the detector to The light intensity that can be detected is 33.

A simple introduction diagram shown below
![diagram for 4 4 custom visualizer 2](https://user-images.githubusercontent.com/114199800/191887045-0452eae9-2a46-4d94-a39d-09770efb6443.jpg)
As When I turn the light source controller one gear counterclockwise, the light source is enhanced by one gear, the editor will show "Brighter". On the other hand, the eidtor will show "Darker" Until the system off.

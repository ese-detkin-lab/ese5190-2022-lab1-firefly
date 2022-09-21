University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Xingqi Pan
        LinkedIn: https://www.linkedin.com/in/xingqipan
    Tested on: MacBook Pro (14-inch, 2021), macOS Monterey 12.5.1

Content:
- Section 3.2 Firefly 
    - Description: Firefly-like light flashing with RP2040 and APDS9960
    - Details:
        
    - Visualization:
    
- Section 4.4 Custom real-time visualizer: Smart Keyboard with RP2040 and APDS9960
    - Description: Using RP2040 to control PC keyboard input and cursor movement with proximity, luminous and gesture data sensed by APDS9960
    - Details:<br />
        This embedded system mainly aims to contrust a smart kerboard with only human interaction. This kind of design can help people, espectially disabled people, to record their thoughts and ideas easily on computer. <br />
        To do this, we use three components:<br />
            - APDS9960: Sensing human interaction data (luminous, gesture, proximity, etc.)<br />
            - RP2040: Compiling and running a Python program to transfer interaction data to computer control instruction.<br />
            - PC: receive the instrucions and take actions.<br />
        The architecture of this embedded system is shown below in the diagram.<br />
        [Diagram here]
        From the diagram above, we can split the structure into four part:<br />
            - Interaction mode switcher via luminous<br />
                - Collect luminous data on the clear channel as luminous<br />
                - 0 < clear < 30000: Keyboard control mode<br />
                - 30000 < clear < 45000: Mouse control mode<br />
                - 45000 < clear < 65535: cursor control mode<br />
                - clear == 65535: Shut down the program<br />
            - Cursor control mode via gesture<br />
                - If entering cursor control mode, the sensor will stay collecting gesture until it receive a non-zero data.<br />
                - 1: up gesture detected, moving up cursor<br />
                - 2: down gesture detected, moving downcursor<br />
                - 3: left gesture detected, moving left curosr <br />
                - 4: right gesture detected, moving right cursor<br />
            - Keyboard control mode via proximity<br />
                - Divided the proximity with range(0,65535) into 40 steps in range(0-39), each steps represents a keycode for typing letters.<br />
                - Include a-z, 1-9, 0, Enter, Escape, Backspace, Tab, Space<br />
            - Mouse control mode via proximity<br />
                - Using the differece between current proximity data and previous proximity data to move the mouse, then left click mouse.<br />
    - Visualization:


Include lab questions, screenshots, analysis, etc. (Remember, this is public, so don't put anything here you don't want to share with the world.)

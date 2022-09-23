University of Pennsylvania, ESE 5190: Intro to Embedded Systems, Lab 1

    Ang Li 
        E-mail: angliqd@seas.upenn.edu
    Tested on: Lenovo Legion Y7000P (15.6-inch, 2021), windows 11
    
    import board
    from adafruit_apds9960.apds9960 import APDS9960
    import time
    import analogio
    import digitalio
    import usb_hid
    from adafruit_hid.keyboard import Keyboard
    from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
    from adafruit_hid.keycode import Keycode
    import neopixel
    import busio
    import adafruit_apds9960.apds9960

    i2c = board.STEMMA_I2C()
    sensor = APDS9960(i2c)
    sensor.enable_proximity = True
    sensor.enable_gesture = True
    sensor.enable_color = True
    sensor.color_integration_time = 10
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

    time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

    led = digitalio.DigitalInOut(board.SCK)
    led.direction = digitalio.Direction.OUTPUT

    c_min = 0.00
    c_max = 10241.00
    step = (c_max - c_min) / 1000.0

    def steps(axis):
        """ Maps the c-range to 0-1000 """
        return round((axis - c_min) / step)

    print("Game Start!")

    while True:


        r, g, b, c = sensor.color_data

        j=0
        if steps(c)==1000:
            keyboard.press(Keycode.O)
            keyboard.release_all()
            print("Bright!Type a letter O")
            time.sleep(3)
        if steps(c)==0:
            for j in range(0,10):
                if steps(c)==0:
                    time.sleep(0.5)
                else:
                    j=20
                r, g, b, c = sensor.color_data
            if j!=9:
                keyboard.press(Keycode.BACKSPACE)
                keyboard.release_all()
                print("Dark!Delete a letter")
                time.sleep(3)

        if j==9:
            print("Game End")
            break

        gesture = sensor.gesture()
        if gesture == 0x01:
            print("up")
            keyboard.press(82)
            keyboard.release_all()
        elif gesture == 0x02:
            print("down")
            keyboard.press(81)
            keyboard.release_all()
        elif gesture == 0x03:
            print("left")
            keyboard.press(80)
            keyboard.release_all()
        elif gesture == 0x04:
            print("right")
            keyboard.press(79)
            keyboard.release_all()


Our code principle:
We designed a game that can be controlled by gesture and brightness: find the letter “Q” mixed with a bunch of letter “O” and replace them with the letter “O”. When the brightness reaches the lowest step we send a ‘backspace’ command, and when the brightness reaches the highest step we type the letter “o”. This is how we replace the letter “Q” with the letter “O”. If you want to quit this game, just let the sensor sense the lowest step of brightness for five seconds and then you can quit.

First, we create some objects and variables to be used. We know that the range of clear values (i.e. variable c) is 0-10241, so we map the c-range to 0-1000 to facilitate subsequent condition judgment. When everything is ready it will print "Game Start!".

In the main loop, we first get the real time values of r, g, b and c, then determine whether the brightness has reached the highest step (steps(c)=1000) or the lowest step (steps(c)=0). When the brightness reaches the highest step we type the letter “o”. When the brightness reaches the lowest step, we first use a “for” loop to determine if the time to reach the lowest order of brightness is enough for five seconds, if not then jump out of the “for” loop and send a ‘backspace’ command, if yes then we jump out of the main loop to end the game. Afterwards we detect the gesture and send the corresponding command to control the cursor up, down, left and right. Besides, the display can update in “real time” along with your sensor by print corresponding strings, so we can know the spirit of the current operation through the serial port.



![image](https://github.com/AngLi-00/ese5190-2022-lab1-firefly/blob/1962d36c4e6b97844f0391fcda429ba582b27104/schematic%20diagram.jpg)

![image](https://github.com/AngLi-00/ese5190-2022-lab1-firefly/blob/1962d36c4e6b97844f0391fcda429ba582b27104/Function%20clarity.jpg)

![image](https://github.com/AngLi-00/ese5190-2022-lab1-firefly/blob/1962d36c4e6b97844f0391fcda429ba582b27104/firefly.gif)

![image](https://github.com/AngLi-00/ese5190-2022-lab1-firefly/blob/1962d36c4e6b97844f0391fcda429ba582b27104/real-time%20visualizer.gif)






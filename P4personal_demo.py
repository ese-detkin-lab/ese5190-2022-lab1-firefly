import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_apds9960.apds9960

# Set up the sensor
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_gesture = True
sensor.enable_color = False

# The main function
def main():
    # an array of up, down, left, right arrows
    keys_pressed = [
        Keycode.UP_ARROW,
        Keycode.DOWN_ARROW,
        Keycode.LEFT_ARROW,
        Keycode.RIGHT_ARROW,
        Keycode.SPACE,
    ]

    # Sleep for a bit to avoid a race condition on some systems
    time.sleep(1)

    keyboard = Keyboard(usb_hid.devices)

    # For avoid the infinity loop

    while True:
        # get the movement from sensor
        move = get_movement()
        # clear = get_brightness()
        # print (move)
        if move == "up":
            for _ in range(3):
                keyboard.press(keys_pressed[0])
                keyboard.release_all()
        elif move == "down":
            for _ in range(3):
                keyboard.press(keys_pressed[1])
                keyboard.release_all()
        elif move == "left":
            for _ in range(3):
                keyboard.press(keys_pressed[2])
                keyboard.release_all()
        elif move == "right":
            for _ in range(3):
                keyboard.press(keys_pressed[3])
                keyboard.release_all()
        """'
        elif clear < 100:
            led.value = True
            keyboard.press(keys_pressed[4]) 
            keyboard.release_all()
        """
        time.sleep(0.1)


# Get the movement of hands and return the movement with a str to the main function
def get_movement():
    gesture = sensor.gesture()
    if gesture == 0x01:
        return "up"
    elif gesture == 0x02:
        return "down"
    elif gesture == 0x03:
        return "left"
    elif gesture == 0x04:
        return "right"
    # if no movements were detcted
    else:
        return "please move your hand above the sensor"


# For Testing
def get_brightness():
    sensor.color_integration_time = 10
    r, g, b, c = sensor.color_data
    print("Red: {0}, Green: {1}, Blue: {2}, Clear: {3}".format(r, g, b, c))
    return c


if __name__ == "__main__":
    main()

import time
import busio
import board
import usb_hid
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import adafruit_apds9960.apds9960

#set up the sensor
i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_color = True

def main():
    # The Keycode sent for each button, will be paired with a control key
    keys_pressed = [Keycode.O, Keycode.BACKSPACE]

    # The keyboard object!
    time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)
    # For QT Py M0:
    led = digitalio.DigitalInOut(board.SCK)
    led.direction = digitalio.Direction.OUTPUT
    
    while True:
        #get the ambient brightness 
        r, g, b, clear_1 = get_brightness()
        time.sleep(0.1)
        r, g, b, clear_2 = get_brightness()
        #if the brightness increases, press 'O'
        print(f"c1:{clear_1}, c2:{clear_2}")
        if clear_1 < clear_2:
            # Turn on the red LED
            led.value = True
            keyboard.press(keys_pressed[0])
            keyboard.release_all()
        elif clear_1 > clear_2:
            keyboard.press(keys_pressed[1])
            keyboard.release_all()

    
def get_brightness():
    #change the color integration tiosensor
    sensor.color_integration_time = 10
    r, g, b, c = sensor.color_data
    #print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    return r, g, b, c

    
if __name__ == "__main__":
    main()


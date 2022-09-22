import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import neopixel
import busio
import adafruit_apds9960.apds9960
import time

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_color = True
sensor.enable_proximity = True
sensor.enable_gesture = True

sensor.color_integration_time = 37  #the largest value is 37889

time.sleep(1)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

last_axis = 0

on_text = "The light sensor is on!\n"
off_text = "\nThe light sensor is off!\n"
wait_text = "Waiting for action..."


def get_diff(brightness):
    global last_axis
    axis = int(brightness * 20 / 4000)
    axis_diff = axis - last_axis
    last_axis = axis
    return axis_diff

def drawbar(diff):
    if diff > 0:
        for x in range(diff):
            keyboard_layout.write("0")
    elif diff < 0:
        for x in range(0 - diff):
            keyboard_layout.write("\b")

def printtext(text):
    keyboard_layout.write(text)
    time.sleep(1)

def print_gesture(gesture):
    if gesture == 0x01:
        print("up")
    elif gesture == 0x02:
        print("down")
    elif gesture == 0x03:
        print("left")
    elif gesture == 0x04:
        print("right")

def findgesture():
    gesture = sensor.gesture()
    return gesture

time.sleep(5)
keyboard_layout.write("The system is ready, move down to turn on the sensor\n")
printtext(wait_text)

while True:
    if findgesture() == 0x01:
        printtext(on_text)
        while True:
            r, g, b, c = sensor.color_data
            print("c: {}".format(c))
            diff = get_diff(c)
            print("diff: {}".format(diff))
            drawbar(diff)
            if findgesture() == 0x02:
                printtext(off_text)
                printtext(wait_text)
                break
            

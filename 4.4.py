import time
import board
import neopixel
import usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
i2c = board.STEMMA_I2C()
sensor = APDS9960(i2c)
sensor.color_integration_time = 10
mouse = Mouse(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
kbd_layout = KeyboardLayoutUS(kbd)

sensor.enable_proximity = True
sensor.enable_color = True
sensor.enable_gesture = True


init = 0

while True:
    while not sensor.color_data_ready:
        time.sleep(0.005)

    r, g, b, c = sensor.color_data
    # print("r: {}, g: {}, b: {}, c: {}".format(r, g, b, c))

    gesture = sensor.gesture()

    if gesture == 1:
        info = kbd_layout.write('Going up!\n')
        pixels.fill((255,255,0))
        time.sleep(0.3)

    if gesture == 2:
        info = kbd_layout.write('Going down!\n')
        pixels.fill((255, 0, 255))
        time.sleep(0.3)

    if gesture == 3:
        info = kbd_layout.write('Turning left!\n')
        pixels.fill((255, 0, 0))
        time.sleep(0.3)

    if gesture == 4:
        info = kbd_layout.write('Turning right!\n')
        pixels.fill((0, 255, 0))
        time.sleep(0.3)



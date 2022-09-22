# Section 4.4

"""CircuitPython Essentials HID Mouse example"""
import time
import board
import neopixel
import usb_hid
import adafruit_apds9960.apds9960
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Setup connection
i2c = board.STEMMA_I2C() # enable I2C connection bwt APDS-9960 and RP2040
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

# Setup param and service
sensor.enable_proximity = True # Retrieve/Read the currently sensed proximity value
sensor.enable_color = True # Enable color reading
sensor.enable_gesture = True # Enable gesture sensing. read if a gesture was detected and what gesture it was.
mouse = Mouse(usb_hid.devices) # set up a mouse service
kbd = Keyboard(usb_hid.devices) # set up a keyboard service
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1) # define LED on RP2040

# Setup global constant
KEY_RANGE = 40 # Key value range
MOVEMENT_RANGE = 50 # Mouse moving range

# Initialization
proximity_past = 0 # define start luminous
c_past = 0


while True:
    proximity = sensor.proximity
    r, g, b, c = sensor.color_data
    print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    gesture = sensor.gesture()


    # Control LED luminous with luminous sensing data
    lum_now = c/256
    pixels.fill(lum_now)
    
    # If luminous lower than 3000, release everything
    if c == 65535:
        kbd.release_all()
        break
    elif c < 3000:
        kbd.release_all()
    elif c > 40000:
        #cursor moving mode
        # If gesture to right, move cursor to right, and so on.
        while gesture == 0x00:
            gesture = sensor.gesture()
            continue
        if gesture == 0x01:
            print("up")
            kbd.send(Keycode.UP_ARROW)
        elif gesture == 0x02:
            print("down")
            kbd.send(Keycode.DOWN_ARROW)
        elif gesture == 0x03:
            print("left")
            kbd.send(Keycode.LEFT_ARROW)
        elif gesture == 0x04:
            print("right")
            kbd.send(Keycode.RIGHT_ARROW)
    elif 30000 < c < 45000:
        # Mouse Controller mode
        # convert the proximity difference into distance
        while proximity == proximity_past:
            proximity_past = proximity
            proximity = sensor.proximity
        prox2dis = (proximity-proximity_past)/256
        print("Proximity to distance:{0}".format(prox2dis))
        mouse.move(x=-int(prox2dis*MOVEMENT_RANGE))
        mouse.click(Mouse.LEFT_BUTTON)
    else:
        # writing mode
        # Control keyboard using proximity
        if proximity > 0 and proximity > proximity_past and c_past <= 30000:
            print("Distance:{0}".format(proximity))
            key = int(proximity/255*40+4)
            kbd.send(key)

    #record past status
    proximity_past = proximity
    c_past = c

    # Tracking sensor data every 0.5s
    time.sleep(0.5)


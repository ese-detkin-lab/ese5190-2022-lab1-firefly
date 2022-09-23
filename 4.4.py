# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_apds9960.apds9960 import APDS9960

import usb_hid

from adafruit_hid.mouse import Mouse
i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True

# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE
m = Mouse(usb_hid.devices)
while True:
    gesture = apds.gesture()

    if gesture == 0x01:
        print("RIGHT")
        m.move(100, 0, 0)
    elif gesture == 0x02:
        print("LEFT")
        m.move(-100, 0, 0)
    elif gesture == 0x03:
        print("UP")
        m.move(0, -100, 0)
    elif gesture == 0x04:
        print("DOWN")
        m.move(0, 100, 0)
# 在这里写上你的代码 :-)

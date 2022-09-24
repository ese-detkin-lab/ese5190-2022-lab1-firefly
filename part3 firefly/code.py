# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import board
import neopixel
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.STEMMA_I2C()

apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True
apds.enable_color = True
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

# Uncomment and set the rotation if depending on how your sensor is mounted.
# apds.rotation = 270 # 270 for CLUE

apds.color_integration_time = 1
while True:
    r, g, b, c = apds.color_data

    pixels.fill((c, 0, 0))

    print('Clear: {0}'.format(c))

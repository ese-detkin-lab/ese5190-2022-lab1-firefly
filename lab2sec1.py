"""Blinking LED"""
import time
import board
import neopixel

# Print statement
print("test")

# LED Blinking
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    pixels.fill((255, 0, 0))
    time.sleep(0.1)
    pixels.fill((0, 0, 0))
    time.sleep(0.1)

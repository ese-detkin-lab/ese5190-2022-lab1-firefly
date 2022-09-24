import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    pixels.fill((0, 255, 125))
    time.sleep(0.6)
    pixels.fill((255, 0, 125))
    time.sleep(0.6)
    pixels.fill((200, 255, 100))
    time.sleep(0.6)
    pixels.fill((0, 0, 0))
    time.sleep(0.3)

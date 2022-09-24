#Lab 1 section 4.4

"""
ESE 5190 Lab1 Firefly section 4.4
Navit Gill
"""
import time
import analogio
import board
import digitalio
import usb_hid
import adafruit_apds9960.apds9960
from adafruit_hid.mouse import Mouse
import busio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

i2c = busio.I2C(board.SCL1, board.SDA1)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True
sensor.enable_gesture = True


keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard) 

keys_O = Keycode.O
keys_backspace = Keycode.BACKSPACE
keys_A = Keycode.A
keys_B = Keycode.B
keys_C = Keycode.C
keys_D = Keycode.D
keys_E = Keycode.E
keys_F = Keycode.F
keys_G = Keycode.G
keys_H = Keycode.H
keys_I = Keycode.I
keys_J = Keycode.J
keys_K = Keycode.K
keys_L = Keycode.L
keys_M = Keycode.M
keys_N = Keycode.N
keys_P = Keycode.P
keys_Q = Keycode.Q
keys_R = Keycode.R
keys_S = Keycode.S
keys_T = Keycode.T
keys_U = Keycode.U
keys_V = Keycode.V
keys_W = Keycode.W
keys_X = Keycode.X
keys_Y = Keycode.Y
keys_Z = Keycode.Z
keys_space = Keycode.SPACE

gestureArray = []

while True:
    gesture = sensor.gesture()

    if gesture != 0x00:
        gestureArray.append(gesture)
        
        if gestureArray == [1]:
            time.sleep(3)
            gesture = sensor.gesture()
            if gesture != 0x00:
                gestureArray.append(gesture)
                print(gestureArray)
                time.sleep(3)
                gesture = sensor.gesture()
                gestureArray.append(gesture)

                if gestureArray == [1,1,0]:
                    keyboard.press(keys_E)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [1,2,0]:
                    keyboard.press(keys_F)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [1,3,0]:
                    keyboard.press(keys_G)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [1,4,0]:
                    keyboard.press(keys_H)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [1,1,1]:
                    keyboard.press(keys_U)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [1,1,2]:
                    keyboard.press(keys_V)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [1,1,3]:
                    keyboard.press(keys_W)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [1,1,4]:
                    keyboard.press(keys_X)
                    keyboard.release_all()
                    gestureArray = []

            else:
                keyboard.press(keys_A)
                keyboard.release_all()
                print(gestureArray)
                gestureArray = []
                
        elif gestureArray == [2]:
            time.sleep(3)
            gesture = sensor.gesture()
            if gesture != 0x00:
                gestureArray.append(gesture)
                print(gestureArray)
                time.sleep(3)
                gesture = sensor.gesture()
                gestureArray.append(gesture)

                if gestureArray == [2,1,0]:
                    keyboard.press(keys_I)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [2,2,0]:
                    keyboard.press(keys_J)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [2,3,0]:
                    keyboard.press(keys_K)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [2,4,0]:
                    keyboard.press(keys_L)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [2,1,1]:
                    keyboard.press(keys_Y)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [2,1,2]:
                    keyboard.press(keys_Z)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [2,1,3]:
                    keyboard.press(keys_space)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [2,1,4]:
                    keyboard.press(keys_backspace)
                    keyboard.release_all()
                    gestureArray = []
            else:
                keyboard.press(keys_B)
                keyboard.release_all()
                print(gestureArray)
                gestureArray = []

        elif gestureArray == [3]:
            time.sleep(3)
            gesture = sensor.gesture()
            if gesture != 0x00:
                gestureArray.append(gesture)
                print(gestureArray)
                time.sleep(3)
                gesture = sensor.gesture()
                gestureArray.append(gesture)

                if gestureArray == [3,1,0]:
                    keyboard.press(keys_M)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [3,2,0]:
                    keyboard.press(keys_N)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [3,3,0]:
                    keyboard.press(keys_O)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [3,4,0]:
                    keyboard.press(keys_P)
                    keyboard.release_all()
                    gestureArray = []
                
            else:
                keyboard.press(keys_C)
                keyboard.release_all()
                print(gestureArray)
                gestureArray = []

        elif gestureArray == [4]:
            time.sleep(3)
            gesture = sensor.gesture()
            if gesture != 0x00:
                gestureArray.append(gesture)
                print(gestureArray)
                time.sleep(3)
                gesture = sensor.gesture()
                gestureArray.append(gesture)

                if gestureArray == [4,1,0]:
                    keyboard.press(keys_Q)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [4,2,0]:
                    keyboard.press(keys_R)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [4,3,0]:
                    keyboard.press(keys_S)
                    keyboard.release_all()
                    gestureArray = []
                elif gestureArray == [4,4,0]:
                    keyboard.press(keys_T)
                    keyboard.release_all()
                    gestureArray = []
                
            else:
                keyboard.press(keys_D)
                keyboard.release_all()
                print(gestureArray)
                gestureArray = []
    
    
    

    

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.

print("importing parts")
from board import SCL, SDA
import busio
import os 
import math

__dirname__ = os.path.dirname(os.path.abspath(__file__))
print(__dirname__.replace("/source-code", ""),__file__)

from time import sleep

print("Variable Initialisation")

from setup import *
from commands import *

# # Import the PCA9685 module.
# from adafruit_pca9685 import PCA9685
# from adafruit_servokit import ServoKit

# print("Variable Initialisation")
# kit = ServoKit(channels=16)

# # Create the I2C bus interface.
# i2c_bus = busio.I2C(SCL, SDA)

# # Create a simple PCA9685 class instance.
# pca = PCA9685(i2c_bus)

# # Set the PWM frequency to 60hz.
# pca.frequency = 60

# Set the PWM duty cycle for channel zero to 50%. duty_cycle is 16 bits to match other PWM objects
# but the PCA9685 will only actually give 12 bits of resolution.


print("System begins to run!")






# print("Serong Kanan")
# pca.channels[4].duty_cycle = 0x0000
# pca.channels[5].duty_cycle = 0xFFFE

# pca.channels[6].duty_cycle = 0x0000
# pca.channels[7].duty_cycle = 0x0000

# pca.channels[8].duty_cycle = 0xFFFE
# pca.channels[9].duty_cycle = 0x0000

# pca.channels[10].duty_cycle = 0x0000
# pca.channels[11].duty_cycle = 0x0000

def setSpeed(percentage: float):
    max = 65535
    half = math.floor(max/2)

    val = percentage * max

    return hex(val)

def findDistance(topPos):
    val = 60 * topPos / 580

    return math.floor(val)

def setDuration(topPos):
    pass

wheels = Wheels(pca)
print("System runs!")
while True:
    # kit.servo[12].angle = 0

    # sleep(2)
    # kit.servo[12].angle = 180
    # sleep(1)
    # print("PCA", pca)
    # wheels.backward()

    # sleep(1)

    # wheels.rotateClockwise()
    # sleep(2)

    # wheels.rotateCounterClockwise()
    # sleep(2)
    # print("Testing Front Wheels to go backward")

    # print("Rotate clockwise")
    # pca.channels[4].duty_cycle = 0xAFFF
    # pca.channels[5].duty_cycle = 0x000

    # pca.channels[6].duty_cycle = 0x0000
    # pca.channels[7].duty_cycle = 0xAFFF

    # pca.channels[8].duty_cycle = 0x0000
    # pca.channels[9].duty_cycle = 0xAFFF

    # pca.channels[10].duty_cycle = 0xAFFF
    # pca.channels[11].duty_cycle = 0x0000

    # pca.channels[13].duty_cycle = 0x0000
    # pca.channels[14].duty_cycle = 0x7FFF # naik
    # pca.channels[0].duty_cycle = 0x0000
    # pca.channels[1].duty_cycle = 0x0000 # naik

    wheels.forward(0xFFFF)

    # sleep(2)

    # pca.channels[13].duty_cycle = 0x000
    # pca.channels[14].duty_cycle = 0xFFFE # naik

    # sleep(2)

    # pca.channels[13].duty_cycle = 0x000
    # pca.channels[14].duty_cycle = 0xFFFE

    # sleep(1)



# try:
#     while True:
#         print("Angle 0!")
#         kit.servo[12].angle = 0
    
#         pca.channels[0].duty_cycle = 0x000
#         pca.channels[1].duty_cycle = 0xFFE

#         pca.channels[13].duty_cycle = 0x000
#         pca.channels[14].duty_cycle = 0xFFFE

#         sleep(1)
#         pca.channels[13].duty_cycle = 0x000
#         pca.channels[14].duty_cycle = 0x000  


#         print("Testing Front Wheels to go forward")
#         pca.channels[6].duty_cycle = 0xFFFE
#         pca.channels[7].duty_cycle = 0x000

#         pca.channels[4].duty_cycle = 0xFFFE
#         pca.channels[5].duty_cycle = 0x000


#         pca.channels[8].duty_cycle = 0xFFFE
#         pca.channels[9].duty_cycle = 0x000

#         pca.channels[10].duty_cycle = 0xFFFE
#         pca.channels[11].duty_cycle = 0x000

#         pca.channels[2].duty_cycle = 0xFFFE
#         pca.channels[3].duty_cycle = 0x0000

#         sleep(3)

#         print("Testing Front Wheels to go backward")
#         pca.channels[6].duty_cycle = 0x000
#         pca.channels[7].duty_cycle = 0xFFFE

#         pca.channels[4].duty_cycle = 0x000
#         pca.channels[5].duty_cycle = 0xFFFE


#         pca.channels[8].duty_cycle = 0x000
#         pca.channels[9].duty_cycle = 0xFFFE

#         pca.channels[10].duty_cycle = 0x000
#         pca.channels[11].duty_cycle = 0xFFFE

#         sleep(3)

#         print("Serong Kiri")
#         pca.channels[6].duty_cycle = 0xFFFE
#         pca.channels[7].duty_cycle = 0x0000

#         pca.channels[4].duty_cycle = 0x000
#         pca.channels[5].duty_cycle = 0xFFFE


#         pca.channels[8].duty_cycle = 0x000
#         pca.channels[9].duty_cycle = 0xFFFE

#         pca.channels[10].duty_cycle = 0xFFFE
#         pca.channels[11].duty_cycle = 0x0000

#         sleep(3)
#         print("Serong Kanan")
#         pca.channels[6].duty_cycle = 0x000
#         pca.channels[7].duty_cycle = 0xFFFE

#         pca.channels[4].duty_cycle = 0xFFFE
#         pca.channels[5].duty_cycle = 0x0000


#         pca.channels[8].duty_cycle = 0xFFFE
#         pca.channels[9].duty_cycle = 0x0000

#         pca.channels[10].duty_cycle = 0x000
#         pca.channels[11].duty_cycle = 0xFFFE


#         sleep(3)

#         print("45 Angle!")
#         kit.servo[12].angle = 45

#         print("Serong (to the right)")
#         pca.channels[4].duty_cycle = 0xFFFE
#         pca.channels[5].duty_cycle = 0x000

#         pca.channels[6].duty_cycle = 0x0000
#         pca.channels[7].duty_cycle = 0x0000

#         pca.channels[8].duty_cycle = 0xFFFE
#         pca.channels[9].duty_cycle = 0x0000

#         pca.channels[10].duty_cycle = 0x0000
#         pca.channels[11].duty_cycle = 0x0000
#         sleep(3)
#         print("90 Angle!")
#         kit.servo[12].angle = 90



#         sleep(3)
#         print("180 angle!")
#         kit.servo[12].angle = 180
#         print("Rotate counter-clockwise")
#         pca.channels[4].duty_cycle = 0x0000
#         pca.channels[5].duty_cycle = 0xFFFE

#         pca.channels[6].duty_cycle = 0x0000
#         pca.channels[7].duty_cycle = 0x0000

#         pca.channels[8].duty_cycle = 0xFFFE
#         pca.channels[9].duty_cycle = 0x0000

#         pca.channels[10].duty_cycle = 0x0000
#         pca.channels[11].duty_cycle = 0x0000
#         sleep(3)   

#         print("Serong Kanan")
#         pca.channels[4].duty_cycle = 0x0000
#         pca.channels[5].duty_cycle = 0xFFFE

#         pca.channels[6].duty_cycle = 0x0000
#         pca.channels[7].duty_cycle = 0x0000

#         pca.channels[8].duty_cycle = 0xFFFE
#         pca.channels[9].duty_cycle = 0x0000

#         pca.channels[10].duty_cycle = 0x0000
#         pca.channels[11].duty_cycle = 0x0000
#         sleep(3)    
# except KeyboardInterrupt:
#     kit.servo[12].angle = 45
#     # kit.continuous_servo[12].throttle = 0

#     print("Keyboard Interrupt!")
#     pca.channels[4].duty_cycle = 0x0000
#     pca.channels[5].duty_cycle = 0x0000

#     pca.channels[6].duty_cycle = 0x0000
#     pca.channels[7].duty_cycle = 0x0000

#     pca.channels[8].duty_cycle = 0x0000
#     pca.channels[9].duty_cycle = 0x0000

#     pca.channels[10].duty_cycle = 0x0000
#     pca.channels[11].duty_cycle = 0x0000
#     pca.channels[11].duty_cycle = 0x0000

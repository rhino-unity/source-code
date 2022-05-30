from board import SCL, SDA
import busio

from adafruit_pca9685 import PCA9685

import commands
import utils.secondsToMs

# Create the I2C bus interface.
i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
pca.frequency = 60

# import servo kit
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
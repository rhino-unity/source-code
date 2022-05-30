from typing import List 
from adafruit_pca9685 import PCA9685 as PCA



class Motor:
    def __init__(self, i2cdevice: PCA, ch1, ch2):
        self.chone = ch1
        self.chtwo = ch2
        self.device = i2cdevice
        self.speedChone = 0x7FFF
        self.speedChtwo = 0x7FFF

    def stop(self):
        self.device.channels[self.chone].duty_cyle = 0
        self.device.channels[self.chtwo].duty_cyle = 0

    def forward(self):
        self.device.channels[self.chone].duty_cyle = self.speedChone
        self.device.channels[self.chtwo].duty_cyle = 0

    def backward(self):
        self.device.channels[self.chone].duty_cyle = 0
        self.device.channels[self.chtwo].duty_cyle = self.speedChtwo

class L298N:
    def __init__(self, i2cdevice: PCA, ch: List[int]):
        self.device = i2cdevice
        self.leftMotor = Motor(i2cdevice, ch[0], ch[1])
        if len(ch) > 3:
            self.rightMotor = Motor(i2cdevice, ch[2], ch[3])
        else:
            self.rightMotor = None

    def __getitem__(self, index):
        if index == 0:
            return self.leftMotor
        elif index == 1:
            return self.rightMotor
        else:
            raise IndexError('index out of range')
    

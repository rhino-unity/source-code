from typing import List 
from adafruit_pca9685 import PCA9685 as PCA
from setup import pca

class Motor:
    def __init__(self, ch1, ch2):
        self.chone = ch1
        self.chtwo = ch2
        # pca.channels[6].duty_cycle = 0xFFFE
        # pca.channels[7].duty_cycle = 0x000

        # pca.channels[4].duty_cycle = 0xFFFE
        # pca.channels[5].duty_cycle = 0x000


        # pca.channels[8].duty_cycle = 0xFFFE
        # pca.channels[9].duty_cycle = 0x000

        # pca.channels[10].duty_cycle = 0xFFFE
        # pca.channels[11].duty_cycle = 0x000


    def stop(self):
        pca.channels[self.chone].duty_cyle = 0x0000
        pca.channels[self.chtwo].duty_cyle = 0x0000

    def forward(self, speed= 0xFFFE):
        print("forward!", pca.channels, self.chone, self.chtwo)
        pca.channels[self.chone].duty_cyle = speed
        pca.channels[self.chtwo].duty_cyle = 0x0000

    def backward(self, speed= 0xFFFE):
        print(speed)
        pca.channels[4].duty_cyle = 0x0000
        pca.channels[5].duty_cyle = speed

class L298N:
    def __init__(self, i2cdevice: PCA, ch: List[int]):
        print(i2cdevice)
        self.leftMotor = Motor( ch[0], ch[1])
        if len(ch) > 3:
            self.rightMotor = Motor( ch[2], ch[3])
        else:
            self.rightMotor = None

    def __getitem__(self, index):
        if index == 0:
            print("left wheel!")
            return self.leftMotor
        elif index == 1:
            return self.rightMotor
        else:
            raise IndexError('index out of range')
    

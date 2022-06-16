from commands.l298n import L298N, Motor
from setup import pca

class Wheels:
    def __init__(self, pca):
        pass
        # self.leftMotorFront = Motor( 4, 5)
        # self.rightMotorFront = Motor( 6, 7)

        # self.leftMotorBack = Motor( 8, 9)
        # self.rightMotorBack = Motor( 10, 11)

        # self.motorDepan = L298N(pca , [4, 5, 6,7]) #
        # self.motorBelakang = L298N(pca , [8, 9, 10, 11])

    def stop(self):
        pca.channels[6].duty_cycle = 0x000
        pca.channels[7].duty_cycle = 0x000

        pca.channels[4].duty_cycle = 0x000
        pca.channels[5].duty_cycle = 0x0000


        pca.channels[8].duty_cycle = 0x000
        pca.channels[9].duty_cycle = 0x0000

        pca.channels[10].duty_cycle = 0x000
        pca.channels[11].duty_cycle = 0x000

    def rotateCounterClockwise(self,  speed=0xAFFF):
        pca.channels[4].duty_cycle = 0x0000
        pca.channels[5].duty_cycle = speed

        pca.channels[6].duty_cycle = speed
        pca.channels[7].duty_cycle = 0x0000

        pca.channels[8].duty_cycle = speed
        pca.channels[9].duty_cycle = 0x0000

        pca.channels[10].duty_cycle = 0x0000
        pca.channels[11].duty_cycle = speed

    def rotateClockwise(self, speed=0xAFFF):
        pca.channels[4].duty_cycle = speed
        pca.channels[5].duty_cycle = 0x000

        pca.channels[6].duty_cycle = 0x0000
        pca.channels[7].duty_cycle = speed

        pca.channels[8].duty_cycle = 0x0000
        pca.channels[9].duty_cycle = speed

        pca.channels[10].duty_cycle = speed
        pca.channels[11].duty_cycle = 0x0000

    def serongKanan(self):
        pca.channels[6].duty_cycle = 0x000
        pca.channels[7].duty_cycle = 0xFFFE

        pca.channels[4].duty_cycle = 0xFFFE
        pca.channels[5].duty_cycle = 0x0000


        pca.channels[8].duty_cycle = 0xFFFE
        pca.channels[9].duty_cycle = 0x0000

        pca.channels[10].duty_cycle = 0x000
        pca.channels[11].duty_cycle = 0xFFFE
        
    def serongKiri(self):
        pca.channels[6].duty_cycle = 0xFFFE
        pca.channels[7].duty_cycle = 0x0000

        pca.channels[4].duty_cycle = 0x000
        pca.channels[5].duty_cycle = 0xFFFE


        pca.channels[8].duty_cycle = 0x000
        pca.channels[9].duty_cycle = 0xFFFE

        pca.channels[10].duty_cycle = 0xFFFE
        pca.channels[11].duty_cycle = 0x0000


    def backward(self):
        pca.channels[6].duty_cycle = 0x000
        pca.channels[7].duty_cycle = 0xFFFE

        pca.channels[4].duty_cycle = 0x000
        pca.channels[5].duty_cycle = 0xFFFE


        pca.channels[8].duty_cycle = 0x000
        pca.channels[9].duty_cycle = 0xFFFE

        pca.channels[10].duty_cycle = 0x000
        pca.channels[11].duty_cycle = 0xFFFE

    def forward(self, speed = 0xFFFE):
        pca.channels[6].duty_cycle = speed
        pca.channels[7].duty_cycle = 0x000

        pca.channels[4].duty_cycle = speed
        pca.channels[5].duty_cycle = 0x000


        pca.channels[8].duty_cycle = speed
        pca.channels[9].duty_cycle = 0x000

        pca.channels[10].duty_cycle = speed
        pca.channels[11].duty_cycle = 0x000

        pca.channels[2].duty_cycle = speed
        pca.channels[3].duty_cycle = 0x0000



    


from commands.l298n import L298N
from setup import pca

class Wheels:
    def __init__(self):
        self.motorDepan = L298N(pca , [4, 5, 6,7]) #
        self.motorBelakang = L298N(pca , [8, 9, 10, 11])


    def rotate360toRight(self):
        pass


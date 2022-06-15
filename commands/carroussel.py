from setup import pca
from commands.l298n import L298N, Motor


# carrousselPin = [11,12]
carroussel = Motor(pca, 2,3)

def startRotate():
    carroussel.forward()

def stopRotate():
    carroussel.stop()

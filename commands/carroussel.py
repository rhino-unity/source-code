from setup import pca
from commands.l298n import L298N, Motor


carrousselPin = [11,12]
carroussel = Motor(pca, carrousselPin[0], carrousselPin[1])

def startRotate():
    pca.device.channels[carrousselPin[0]] = 0x7FFF
    pca.device.channels[carrousselPin[1]] = 0x0000

def stopRotate():
    pca.device.channels[carrousselPin[0]] = 0x0000
    pca.device.channels[carrousselPin[1]] = 0x0000
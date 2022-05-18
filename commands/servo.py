from adafruit_servokit import ServoKit

class Servos:
    def __init__(self, chns: 16):
        self.servos = ServoKit(chns)

    def fingers_get(self):
        pass
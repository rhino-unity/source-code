from setup import *


# Import ServiKit
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


# jetson.inference object detection
# import jetson.inference
# import jetson.utils
import time

# net = jetson.inference.detectNet(argv=['--model=models/CT2/ssd-mobilenet.onnx', '--labels=models/CT2/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--threshold=0.4', '--output-bbox=boxes'])
# camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")
# display = jetson.utils.glDisplay()

statusGame = "standby" # standby | running | 
start_time = 0


def runGame():
    while True:
        remaining = time.time() - start_time 
        
        if remaining == utils.secondsToMs.secondsToMs(155):
            print("Game Ended")
            return
        


while True:
    if statusGame == "standby":
        answer = input("Start Robot? (Y/n)")

        if answer != 'Y' or answer != 'n':
            continue
        
        if answer == 'Y':
            statusGame = "running"
            start_time = time.time()

        if answer == "n":
            statusGame = "standby"
            continue
    
    if statusGame == "running":
        runGame()
        continue
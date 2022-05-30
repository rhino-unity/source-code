print("Initial Setup, importing..")
from setup import *
from commands import *
import utils.secondsToMs

print("Success Initial Setup!")

# jetson.inference object detection
# import jetson.inference
# import jetson.utils
import time

# net = jetson.inference.detectNet(argv=['--model=models/CT2/ssd-mobilenet.onnx', '--labels=models/CT2/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--threshold=0.4', '--output-bbox=boxes'])
# camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")
# display = jetson.utils.glDisplay()

global statusGame 
statusGame = "standby" # standby | running | 
start_time = 0

# wheels = Wheels()

# idk = Motor(pca, 4,5)
# idk2 = Motor(pca, 6,7)

def runGame():
    while True:
        remaining = time.time() - start_time 

        pca.channels[4].duty_cycle = 0x7FFF
        pca.channels[5].duty_cycle = 0x0000
        # idk.forward()
        # idk2.backward()

        # wheels.motorDepan[0].forward()
        # wheels.motorDepan[1].forward()

        # wheels.motorDepan

        if remaining == utils.secondsToMs.secondsToMs(155):
            print("Game Ended")
            return
        

while True:
    if statusGame == "standby":

        answer = input("Start Robot? (Y/n)")
        # print(answer)
        
        if answer == 'Y':
            # print("yess")
            statusGame = "running"
            start_time = time.time()

        if answer == "n":
            statusGame = "standby"
            continue

        if answer != 'Y' or answer != 'n':
            print('yo')
            continue
    
    if statusGame == "running":
        runGame()
        continue
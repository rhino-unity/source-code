import time
import os
from math import floor
from adafruit_rplidar import RPLidar


# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, timeout=3)

# used to scale data to fit on the screen
max_distance = 0

writeStatus = 1

i = 0

def process_data(data):
    print(data)

def writeFile(data):
    converted_data = str(data)
    if i == 20:
       #clipboard.copy(converted_data)
       #print("copy ke clipboard")

       with open("demofile2.txt",'w') as f:
           pass
       f = open("demofile2.txt", "a")
       #converted_data = str(data)
       print("write file")
       f.write(converted_data)
       f.close()
       #writeStatus = 0


scan_data = [0]*360
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0 

print('tes')

try:
#    print(lidar.get_info())
	for scan in lidar.iter_scans():
		for (_, angle, distance) in scan:
			scan_data[min([359, floor(angle)])] = distance 
			process_data(scan_data[min([359, 1])])
			writeFile(scan_data[min([2, 1])])
		i = i+1
		print(i)
		if i == 21:
			i = 0

except KeyboardInterrupt:
#    print('Stopping.')
	lidar.stop()
#lidar.stop_motor()
	lidar.disconnect()


# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This simple test outputs a 50% duty cycle PWM single on the 0th channel. Connect an LED and
# resistor in series to the pin to visualize duty cycle changes and its impact on brightness.
from setup import *
from commands import *

from board import SCL, SDA
import busio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685
import os

from pathlib import Path

__dirname__ = Path(os.path.dirname(os.path.abspath(__file__)))
__parent__ = __dirname__.parent.absolute()

# Create the I2C bus interface.
# i2c_bus = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
# pca = PCA9685(i2c_bus)

# Set the PWM frequency to 60hz.
# pca.frequency = 60

# Import ServiKit
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

# jetson.inference object detection
import jetson.inference
import jetson.utils
import time

net = jetson.inference.detectNet(argv=[f'--model={__parent__}/models/CT2/ssd-mobilenet.onnx', f'--labels={__parent__}/models/CT2/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--threshold=0.4', '--output-bbox=boxes'])
camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")
display = jetson.utils.glDisplay()

wheels = Wheels(pca)

start_time = time.time() # Untuk setting hitung waktu selama game berlangsung
hitungWaktu = 0 # Hitung waktu awal game hingga akhir game
hitungWaktu = 35 # posisi awal hitungwaktu diubah langsung menuju awal autonomous 2
durasiWaktu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # Array durasi waktu (array 0-9 untuk autonomous 1) dan (array 10-19 untuk autonomous 2) 
statusGame = "Standby" # Status game: Standby, Running, dll (Fungsi statusGame adalah agar tidak diinterupsi selama status masih berlangsung)
pca.channels[0].duty_cycle = 0x0000 # motor OFF saat awal standby
pca.channels[1].duty_cycle = 0x0000 # motor OFF saat awal standby, nilai channel [0] dan [1] berpasangan untuk menentukan arah putaran motor 
pca.channels[2].duty_cycle = 0x0000 # motor OFF saat awal standby
pca.channels[3].duty_cycle = 0x0000 # motor OFF saat awal standby, nilai channel [2] dan [3] berpasangan untuk menentukan arah putaran motor
pca.channels[8].duty_cycle = 0x0000 # LED 1 OFF
pca.channels[9].duty_cycle = 0x0000 # LED 2 OFF
pca.channels[10].duty_cycle = 0x0000 # LED 3 OFF 
kit.servo[14].angle = 45 # servo untuk lengan naik turun (posisi awal 45 derajat) (level 1 = 0 derajat, level 2 = 45 drajat, level 3 = 90 derajat) 
kit.servo[15].angle = 90 # servo untuk jari gripper (posisi awal menutup = 90) (posisi membuka = 0)

IdObjekTerdeteksi = 0 # ID objek yang terdeteksi (ID class objek hasil training jetson inference)
posisiObjekTerdeteksi = 0 # adalah variabel nilai dalam bentuk bilangan hasil tampilan kamera
statusObjekTerdeteksi = "" # adalah variabel dalam bentuk teks ("Objek di kiri", "Objek di tengah" atau "Objek di kanan") hasil tampilan kamera
levelShippingHub = 0 # level tujuan pada shipping hub (level 1 = bawah, 2 = tengah, 3 = atas) 

def tombolStart(): # Tombol Start
    print('Start Game -- Tekan Enter --')
    x = input()
    print('GO !!!, ' + x)

def tombolUlang(): # Tombol Ulang
    print('Ulang lagi? -- Tekan Enter --')
    x = input()
    print('GO !!!, ' + x)


while display.IsOpen():
    img, width, height = camera.CaptureRGBA()
    detections = net.Detect(img, width, height) 

    # Tombol Start mengubah status game dari Standby menjadi Running
    if statusGame == "Standby" :	
        tombolStart()
        statusGame = "Running"	
    
    # print the detections
    # print("detected {:d} objects in image".format(len(detections)))
    for detection in detections:
        print(detection)
    
        top = detection.Top # with capital letters, just as they are shown by the print() statement.
        IdObjekTerdeteksi = detection.ClassID
        posisiObjekTerdeteksi = detection.Left # titik acuan posisi objek terdeteksi adalah titik sisi kiri objek
        print("ID objek yang terdeteksi",IdObjekTerdeteksi)

        if IdObjekTerdeteksi == 3: # 3 adalah ID untuk objek kubus hasil training jetson inference 
            print('objek kubus terdeteksi')
            if posisiObjekTerdeteksi > 0 and posisiObjekTerdeteksi < 400:
                #print('Objek di kiri')
                statusObjekTerdeteksi = "Objek di kiri"
                # pca.channels[8].duty_cycle = 0x7FFF # LED1 ON
            if posisiObjekTerdeteksi > 400 and posisiObjekTerdeteksi < 800:
                #print('Objek di tengah')
                statusObjekTerdeteksi = "Objek di tengah"
                # pca.channels[9].duty_cycle = 0x7FFF # LED2 ON
            if posisiObjekTerdeteksi > 800 and posisiObjekTerdeteksi < 1280:
                #print('Objek di kanan')
                statusObjekTerdeteksi = "Objek di kanan"
                # pca.channels[10].duty_cycle = 0x7FFF # LED3 ON
            else:
                pass
                
                # pca.channels[8].duty_cycle = 0x0000 # LED 1 OFF
                # pca.channels[9].duty_cycle = 0x0000 # LED 2 OFF
                # pca.channels[10].duty_cycle = 0x0000 # LED 3 OFF			

        if IdObjekTerdeteksi == 1 or IdObjekTerdeteksi == 2:
            print('objek selain kubus terdeteksi')

        else :
            pass
            # Matikan seluruh LED
            # pca.channels[8].duty_cycle = 0x0000 # LED 1 OFF
            # pca.channels[9].duty_cycle = 0x0000 # LED 2 OFF
            # pca.channels[10].duty_cycle = 0x0000 # LED 3 OFF

    display.RenderOnce(img, width, height)
    display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

    # Setting hitung waktu per detik
    waktu = time.time() - start_time
    if waktu > 1:
        start_time = time.time()
        hitungWaktu = hitungWaktu + 1 
        
    # Program Robot selama game berlangsung ********************************************************************************************

        # Waktu game adalah 2 menit 30 detik ditambah waktu standy (5 detik antara autonomos 1 dengan autonomos 2), total = 155 detik
        if hitungWaktu <= 155 :	
            print(hitungWaktu) 

        # Game Autonomous 1 mulai
        if hitungWaktu == 1 :
            print("Game Autonomous 1 mulai")
            levelShippingHub = 0

        # Robot deteksi objek untuk menentukan posisi dropping di shipping hub
        if hitungWaktu > 1 and hitungWaktu < 4 :
            print("Robot deteksi objek untuk menentukan posisi dropping di shipping hub")
            if statusObjekTerdeteksi == "Objek di kiri" :
                print('Shipping hub level 1')
                levelShippingHub = 1
            if statusObjekTerdeteksi == "Objek di tengah" :
                print('Shipping hub level 2')
                levelShippingHub = 2
            if statusObjekTerdeteksi == "Objek di kanan" :
                print('Shipping hub level 3')
                levelShippingHub = 3
            #if statusObjekTerdeteksi == "Tidak ada objek" :
                #print('Level tidak Terdeteksi')

        # Robot maju menuju shipping hub
        if hitungWaktu == 3 :
            print("Robot Maju menuju shipping hub")
            wheels.forward()

        # Robot Berhenti disekitar shipping hub
        if hitungWaktu == 10 :
            print("Robot berhenti disekitar shipping hub")
            wheels.stop()

        # Robot baca data Lidar
        if hitungWaktu == 11 :
            print("Robot bacaLidar")
            f = open("demofile2.txt", "r")
            print(f.read())

        # Robot dropping objek berdasarkan data hasil deteksi objek dan Lidar
        if hitungWaktu == 13 :
            print("Robot dropping objek berdasarkan data hasil deteksi objek dan Lidar")
            print("IF data hasil deteksi adalah level 1 or 2 or 3 THEN ? ...")
            if levelShippingHub == 1 :
                print("motor lengan bergerak ke shiping hub level 1")
                pca.channels[0].duty_cycle = 0x7FFF # motor ON
                pca.channels[1].duty_cycle = 0x0000 # motor ON
                pca.channels[2].duty_cycle = 0x0000 # motor ON
                pca.channels[3].duty_cycle = 0x0000 # motor ON
                kit.servo[14].angle = 0
                kit.servo[15].angle = 0
            if levelShippingHub == 2 :
                print("motor lengan bergerak ke shiping hub level 2")
                pca.channels[0].duty_cycle = 0x7FFF # motor ON
                pca.channels[1].duty_cycle = 0x0000 # motor ON
                pca.channels[2].duty_cycle = 0x0000 # motor ON
                pca.channels[3].duty_cycle = 0x7FFF # motor ON
                kit.servo[14].angle = 45
                kit.servo[15].angle = 0
            if levelShippingHub == 3 :
                print("motor lengan bergerak ke shiping hub level 3")
                pca.channels[0].duty_cycle = 0x0000 # motor ON
                pca.channels[1].duty_cycle = 0x0000 # motor ON
                pca.channels[2].duty_cycle = 0x0000 # motor ON
                pca.channels[3].duty_cycle = 0x7FFF # motor ON
                kit.servo[14].angle = 90
                kit.servo[15].angle = 0

            print("Selanjutnya ke Warehouse atau ke Carousel ? ...")

            print("Robot bergerak dan parking sebelum waktu autonomous 1 berakhir")

        # Robot baca data Lidar selama rentang waktu tertentu
        if hitungWaktu > 17 and hitungWaktu < 27 :
            print("Robot bacaLidar")
            f = open("demofile2.txt", "r")
            print(f.read())

            hasilBacaLidarFloat = []
            g = open('demofile2.txt')
            for line in g.readlines():
                hasilBacaLidarFloat = float(line)
            g.close()
            
            ValidDataLidar = (isinstance(hasilBacaLidarFloat, float))

            if ValidDataLidar == True :
                if hasilBacaLidarFloat > 700 :
                    print("Tidak ada rintangan .. Robot maju")
                    pca.channels[0].duty_cycle = 0x0000 # motor ON
                    pca.channels[1].duty_cycle = 0x7FFF # motor ON
                    pca.channels[2].duty_cycle = 0x7FFF # motor ON
                    pca.channels[3].duty_cycle = 0x0000 # motor ON
                if hasilBacaLidarFloat < 700 :
                    print("Ada rintangan .. Robot Menghindar ")
                    pca.channels[0].duty_cycle = 0x7FFF # motor ON
                    pca.channels[1].duty_cycle = 0x0000 # motor ON
                    pca.channels[2].duty_cycle = 0x7FFF # motor ON
                    pca.channels[3].duty_cycle = 0x0000 # motor ON

        # Robot parking
        if hitungWaktu == 28 :
            print("Robot parking")
            pca.channels[0].duty_cycle = 0x0000 # motor OFF
            pca.channels[1].duty_cycle = 0x0000 # motor OFF
            pca.channels[2].duty_cycle = 0x0000 # motor OFF
            pca.channels[3].duty_cycle = 0x0000 # motor OFF
            print("End Autonomous 1")

        # Robot Standby sebelum Autonomous 2 dimulai selama 5 detik
        if hitungWaktu == 31 :
            print("Standby Autonomous 2")

        # Game Autonomous 2 mulai
        if hitungWaktu == 35 :
            print("Game Autonomous 2 mulai")
            statusObjekTerdeteksi = "Tidak ada objek" # Reset variabel statusObjekTerdeteksi 
            print("Robot mulai mencari,mengabil dan delivery objek selama waktu autonomous 2")
            
                  # Robot kondisi IF THEN
        if hitungWaktu > 35 and hitungWaktu < 124 :
            print("Bagian coding robot AUTONOMOUS mengambil objek")	
            #print("Robot bacaLidar")
            #f = open("demofile2.txt", "r")
            #print(f.read())

            # Robot berputar ke kanan selama 15 detik
            setDurasiWaktuPutarKanan = 15
            if durasiWaktu[10] < setDurasiWaktuPutarKanan :
                print("berputar ke kanan")  
                pca.channels[0].duty_cycle = 0x0000 # motor ON
                pca.channels[1].duty_cycle = 0x5FFF # motor ON
                pca.channels[2].duty_cycle = 0x0000 # motor ON
                pca.channels[3].duty_cycle = 0x5FFF # motor ON
                durasiWaktu[10] = durasiWaktu[10] + 1
                if statusObjekTerdeteksi == "Objek di tengah" :
                    durasiWaktu[10] = (1000) #durasi selesai
                    durasiWaktu[11] = (1000) #durasi selesai
            if durasiWaktu[10] == setDurasiWaktuPutarKanan :
                durasiWaktu[10] = (1000) # durasi selesai

            # Selanjutnya Robot berputar ke kiri selama 15 detik
            setDurasiWaktuPutarKiri = 15
            if durasiWaktu[10] == 1000 and durasiWaktu[11] < setDurasiWaktuPutarKiri :
                print("berputar ke kiri") 
                pca.channels[0].duty_cycle = 0x5FFF # motor ON
                pca.channels[1].duty_cycle = 0x0000 # motor ON
                pca.channels[2].duty_cycle = 0x5FFF # motor ON
                pca.channels[3].duty_cycle = 0x0000 # motor ON
                durasiWaktu[11] = durasiWaktu[11] + 1
                if statusObjekTerdeteksi == "Objek di tengah" :
                    durasiWaktu[10] = (1000) # durasi selesai
                    durasiWaktu[11] = (1000) # durasi selesai
            if durasiWaktu[11] == setDurasiWaktuPutarKiri :
                durasiWaktu[11] = (1000) # durasi selesai

            # Seluruh urutan durasi waktu selesai, robot melanjutkan 
            if durasiWaktu[10] == 1000 and durasiWaktu[11] == 1000 :
                setDurasiWaktuJariAmbilObjek = 2 # saat durasi 2 detik servo jari akan mengambil objek
                setAkhirWaktusebelumUlangLagi = 10 # setelah 10 detik akan mengulang lagi mencari objek
                if durasiWaktu[12] < setDurasiWaktuJariAmbilObjek : 
                    print("berhenti") 
                    pca.channels[0].duty_cycle = 0x0000 # motor OFF
                    pca.channels[1].duty_cycle = 0x0000 # motor OFF
                    pca.channels[2].duty_cycle = 0x0000 # motor OFF
                    pca.channels[3].duty_cycle = 0x0000 # motor OFF
                    print("Jari membuka untuk mengambil objek kubus")
                    kit.servo[14].angle = 140
                    kit.servo[15].angle = 0		
                if durasiWaktu[12] == setDurasiWaktuJariAmbilObjek :
                    # Servo		
                    kit.servo[14].angle = 45 
                    kit.servo[15].angle = 140
                if durasiWaktu[12] == setDurasiWaktuJariAmbilObjek + 2 : 
                    # Servo jari menutup
                    print("Jari menutup mengambil objek kubus")
                    kit.servo[15].angle = 0
                if durasiWaktu[12] == setDurasiWaktuJariAmbilObjek + 3 : 
                    # Servo naik
                    kit.servo[14].angle = 140
                if durasiWaktu[12] > setDurasiWaktuJariAmbilObjek and hitungWaktu < 124 :
                    # Robot maju dan delivery objek ... coding diubah sesuai kebutuhan
                    # Harus ada sensor microswitch 
                    print("Robot bacaLidar")
                    f = open("demofile2.txt", "r")
                    print(f.read())
                    hasilBacaLidarFloat = []
                    g = open('demofile2.txt')
                    for line in g.readlines():
                        hasilBacaLidarFloat = float(line)
                    g.close()

                    ValidDataLidar = (isinstance(hasilBacaLidarFloat, float))

                    if ValidDataLidar == True :
                        if hasilBacaLidarFloat > 700 :
                            print("Tidak ada rintangan .. Robot maju")
                            pca.channels[0].duty_cycle = 0x0000 # motor ON
                            pca.channels[1].duty_cycle = 0x7FFF # motor ON
                            pca.channels[2].duty_cycle = 0x7FFF # motor ON
                            pca.channels[3].duty_cycle = 0x0000 # motor ON
                        if hasilBacaLidarFloat < 700 :
                            print("Ada rintangan .. Robot Menghindar ")
                            pca.channels[0].duty_cycle = 0x7FFF # motor ON
                            pca.channels[1].duty_cycle = 0x0000 # motor ON
                            pca.channels[2].duty_cycle = 0x7FFF # motor ON
                            pca.channels[3].duty_cycle = 0x0000 # motor ON
                    
                durasiWaktu[12] = durasiWaktu[12] + 1
                if durasiWaktu[12] == setAkhirWaktusebelumUlangLagi :
                    kit.servo[15].angle = 0
                    statusObjekTerdeteksi = "Tidak ada objek" # Reset variabel statusObjekTerdeteksi 
                    durasiWaktu[10] = (0) # durasi loop lagi
                    durasiWaktu[11] = (0) # durasi loop lagi
                    durasiWaktu[12] = (0) # durasi loop lagi


        if hitungWaktu == 125 :				
            hitungWaktu = 35 # posisi awal hitungwaktu diulang menuju awal autonomous 2

        """
        # Memasuki End Game Period Running
        if hitungWaktu == 125 :
            print("Memasuki End Game Period Running")
            print("Robot memutar Carousel atau bergerak mengambil dan delivery objek")
            print("Robot parking sebelum waktu autonomous 2 berakhir")
            pca.channels[0].duty_cycle = 0x7FFF # motor ON
            pca.channels[1].duty_cycle = 0x0000 # motor ON
            pca.channels[2].duty_cycle = 0x0000 # motor ON
            pca.channels[3].duty_cycle = 0x7FFF # motor ON

        # Robot parking
        if hitungWaktu == 154 :
            print("Robot parking")
            pca.channels[0].duty_cycle = 0x0000 # motor OFF
            pca.channels[1].duty_cycle = 0x0000 # motor OFF
            pca.channels[2].duty_cycle = 0x0000 # motor OFF
            pca.channels[3].duty_cycle = 0x0000 # motor OFF

        # Game Over
        if hitungWaktu == 155 :
            print("End Autonomous 2")
            print("-- Game Over --")

        """

        # End Program Robot selama game berlangsung **********************************************************************************

        # Mulai Lagi
        if hitungWaktu > 200 :
            pca.channels[8].duty_cycle = 0x7FFF # LED 1 ON
            pca.channels[9].duty_cycle = 0x07FFF # LED 2 ON
            pca.channels[10].duty_cycle = 0x7FFF # LED 3 ON 
            tombolUlang()
            pca.channels[0].duty_cycle = 0x0000 # motor OFF awal standby
            pca.channels[1].duty_cycle = 0x0000 # motor OFF awal standby
            pca.channels[2].duty_cycle = 0x0000 # motor OFF awal standby
            pca.channels[3].duty_cycle = 0x0000 # motor OFF awal standby
            pca.channels[8].duty_cycle = 0x0000 # LED 1 OFF
            pca.channels[9].duty_cycle = 0x0000 # LED 2 OFF
            pca.channels[10].duty_cycle = 0x0000 # LED 3 OFF 
            kit.servo[14].angle = 45 # servo untuk lengan naik turun (posisi awal 45 derajat) 
            kit.servo[15].angle = 90 # servo untuk jari gripper (posisi awal menutup = 90)
            IdObjekTerdeteksi = 0 # kembali ke 0
            posisiObjekTerdeteksi = 0 # kembali ke 0
            statusObjekTerdeteksi = "" # kembali ke 0
            levelShippingHub = 0 # kembali ke 0
            durasiWaktu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # kembali ke 0
            hitungWaktu = 0 # kembali ke 0
            


# jetson.inference object detection
import jetson.inference
import jetson.utils
import os

from pathlib import Path

__dirname__ = Path(os.path.dirname(os.path.abspath(__file__)))
__parent__ = __dirname__.parent.absolute()


net = jetson.inference.detectNet(argv=[f'--model={__parent__}/models/CT2/ssd-mobilenet.onnx', f'--labels={__parent__}/models/CT2/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--threshold=0.4', '--output-bbox=boxes'])
camera = jetson.utils.gstCamera(1280, 720, "/dev/video0")
display = jetson.utils.glDisplay()


while display.IsOpen():
    img, width, height = camera.CaptureRGBA()
    detections = net.Detect(img, width, height) 


    for detection in detections:
        print(detection)

        top = detection.Top
        IdObjekTerdeteksi = detection.ClassID
        posisiObjekTerdeteksi = detection.Left # titik acuan posisi objek terdeteksi adalah titik sisi kiri objek

        print("ID objek yang terdeteksi",IdObjekTerdeteksi)
    display.RenderOnce(img, width, height)
    display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
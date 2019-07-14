
from imageai.Detection import ObjectDetection
import os
import  cv2
cap=cv2.VideoCapture(0)

while True:
    status,frame=cap.read()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
    detector.loadModel()
    print(dir(detector))
    detections = detector.detectObjectsFromImage(input_image=frame, output_image_path="imagenewooo.jpg")

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

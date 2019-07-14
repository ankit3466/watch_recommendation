from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="cat.jpg", output_image_path="imagenew.jpg")

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

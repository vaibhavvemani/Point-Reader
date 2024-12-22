from ultralytics import YOLO
import cv2

def detect_pen(image_path):
    model = YOLO('yolov8n.pt')
    results = model(image_path)
    return results


results = detect_pen('Dataset/cat.png')

for result in results:
    boxes = result.boxes 
    masks = result.masks  
    keypoints = result.keypoints  
    probs = result.probs  
    obb = result.obb  
    result.show()  
    result.save(filename="result.jpg") 
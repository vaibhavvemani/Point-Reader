from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='C:/Users/vaibh/Projects/Finals/point-reader/app/penDetection/Dataset/data.yaml',
   imgsz=640,
   epochs=10,
   batch=8,
   name='yolov8n_custom'
)
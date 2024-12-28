from ultralytics import YOLO
import cv2

model_name = 'yolov8n.pt'
model_name2 = 'C:/Users/vaibh/Projects/Finals/point-reader/app/runs/detect/yolov8n_custom2/weights/best.pt'
def detect_pen(image_path):
    model = YOLO(model_name)
    results = model(image_path)
    return results


# model = YOLO('C:/Users/vaibh/Projects/Finals/point-reader/app/runs/detect/yolov8n_custom2/weights/best.pt')

# cap = cv2.VideoCapture(0)

# while True:
#     ret, image = cap.read()
#     results = model(image)
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             cv2.rectangle(image, (x1, y1, x2, y2), (255, 0, 0), 2)
#             cv2.putText(image, 'Pen', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
#     cv2.imshow('frame', image)

#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
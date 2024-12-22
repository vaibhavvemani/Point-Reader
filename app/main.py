from image2text.easy import detect_text
from penDetection.yolo import detect_pen
import cv2

image_path = 'C:/Users/vaibh/Projects/Finals/point-reader/app/testdata/person.jpeg'

text_result = detect_text(image_path)
pen_result = detect_pen(image_path)

print(f"Text Detection: {text_result}\n Pen Detection: {pen_result}")

image = cv2.imread(image_path)

# for bbox, text, prob in text_result:
#     cv2.rectangle(image, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)
#     cv2.putText(image, text, (int(bbox[0][0]), int(bbox[0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# for result in pen_result:
#     boxes = result.boxes
#     for box in boxes:
#         x1, y1, x2, y2 = box.xyxy[0]
#         x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#         cv2.rectangle(image, (x1, y1, x2, y2), (255, 0, 0), 2)
#         cv2.putText(image, 'Pen', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# cv2.imwrite('output_with_bounding_boxes.jpg', image)

bounding_box = []

def check_overlap(text_result, pen_result):
    for bbox, text, prob in text_result:
        for result in pen_result:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                if overlap(bbox, [x1, y1, x2, y2]):
                    bounding_box.append(bbox)
                    bounding_box.append([x1, y1, x2, y2])

def overlap (box1, box2):
    x1, y1, x2, y2 = box1
    x3, y3, x4, y4 = box2
    if x3 > x2 or x4 < x1 or y3 > y2 or y4 < y1:
        return False
    return True


for box in bounding_box:
    cv2.rectangle(image, (int(box[0][0]), int(box[0][1])), (int(box[2][0]), int(box[2][1])), (0, 0, 255), 2)

cv2.imwrite('result.jpg', image)
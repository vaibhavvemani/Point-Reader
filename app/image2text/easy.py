# EasyOCR
import easyocr
import cv2

def detect_text(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    return result

# image = cv2.imread("C:/Users/vaibh/Projects/Finals/point-reader/app/penDetection/Dataset/cat.png")
# result = detect_text("C:/Users/vaibh/Projects/Finals/point-reader/app/penDetection/Dataset/cat.png")
# for bbox, text, prob in result:
#     cv2.rectangle(image, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)
#     cv2.putText(image, text, (int(bbox[0][0]), int(bbox[0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# cv2.imwrite('output_with_bounding_boxes.jpg', image)
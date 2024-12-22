# EasyOCR
import easyocr
import cv2

def detect_text(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    return result

# image = cv2.imread(image_path)
# for bbox, text, prob in result:
#     cv2.rectangle(image, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)
#     cv2.putText(image, text, (int(bbox[0][0]), int(bbox[0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# cv2.namedWindow('Image with Bounding Boxes', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Image with Bounding Boxes', 800, 600)
# cv2.imshow('Image with Bounding Boxes', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
from image2text.easy import detect_text
from penDetection.yolo import detect_pen
from api.api import get_meaning
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    text_result = detect_text(image)
    pen_result = detect_pen(image)

    overlap_word = ""

    def check_overlap(box1, box2):
        x1, y1, x2, y2 = box1
        x3, y3, x4, y4 = box2

        if x3 < x2 and x4 > x1 and y3 < y2 and y4 > y1:
            return True
        return False

    for pen in pen_result[0].boxes:
        for bbox, text, prob in text_result:
            if check_overlap(pen.xyxy[0].numpy(), bbox[0]+bbox[2]):
                cv2.rectangle(image, (int(pen.xyxy[0][0]), int(pen.xyxy[0][1])), (int(pen.xyxy[0][2]), int(pen.xyxy[0][3])), (255, 0, 0), 2)
                cv2.rectangle(image, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)
                cv2.putText(image, text, (int(bbox[0][0]), int(bbox[0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                overlap_word = text
                break
    cv2.imwrite('output_with_brush.jpg', image)
    cv2.imshow('image', image)

    # definition = get_meaning(overlap_word)
    # print("overlap_word:", definition)
    print(overlap_word)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



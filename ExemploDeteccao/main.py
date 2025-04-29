#main.py
from ultralytics import YOLO
import cv2

model = YOLO('yolov8x.pt')
img = cv2.imread('cachorro.jpg')
results = model(img)
img_detected = results[0].plot()

cv2.imshow("YOLOv8 Detecção", img_detected)
cv2.waitKey(0)
cv2.destroyAllWindows()

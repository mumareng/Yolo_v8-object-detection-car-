from ultralytics import YOLO
import cv2
# cvzone use to display detectection 
import cvzone 

# use here yolo version 8 neno, model weight=  yolov8l.pt large,small,nano
model = YOLO('yolov8l.pt')
results = model("test.jpg", show=True)

# add delay untill user close it
cv2.waitKey(0)

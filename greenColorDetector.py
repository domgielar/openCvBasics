import cv2
import os
import numpy as np
from util import get_limits
from PIL import Image

brown = [0, 100, 255] #red in BGR colorspace
cap = cv2.VideoCapture(0)

#running webcam
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=brown)
    mask = cv2.inRange(hsvImage,lowerLimit, upperLimit )

    #converting this image into pillow
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1,y1,x2,y2 =bbox
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(60)& 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
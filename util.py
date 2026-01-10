import cv2
import numpy as np


#
#def get_limits(color):
#   c=np.uint8([[color]])#insert bgr values which you want to convert to hsv
 #   hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
#
 #   lowerLimit = hsvC[0][0][0] - 10, 100, 100
 #   upperLimit = hsvC[0][0][0] + 10, 255, 255
#
 #   lowerLimit = np.array(lowerLimit, dtype=np.uint8)
 #   upperLimit = np.array(upperLimit, dtype=np.uint8)
#
 #   return lowerLimit, upperLimit 


def get_limits(color):
    c = np.uint8([[color]])
    hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)[0][0]
    h = int(hsv[0])

    lower_h = max(h - 15, 0)
    upper_h = min(h + 15, 179)

    lower = np.array([lower_h, 20, 20], dtype=np.uint8)
    upper = np.array([upper_h, 255, 255], dtype=np.uint8)
    return lower, upper

import os
import cv2

img = cv2.imread(os.path.join('.','data','paper.png'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



thresh = cv2.adaptiveThreshold(img_gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,51,5)
cv2.imshow("img", img)
cv2.imshow("thresh", thresh)

cv2.waitKey(0)
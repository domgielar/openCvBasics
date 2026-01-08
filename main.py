import cv2
import os 

#Colorspaces

img = cv2.imread(os.path.join(".",'data','drakemaye.jpg'))
#switch the red blue colors or the position of it
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#switch everything to gray so one channel
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#visualize
cv2.imshow('img', img)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_hsv', img_hsv)


cv2.waitKey(0)

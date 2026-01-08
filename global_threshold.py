import os
import cv2

img = cv2.imread(os.path.join('.','data','drakemaye.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#all the pixels below 80 will go to 0 all the pixles above 255 go to 1
ret, img_thresh = cv2.threshold(img_gray, 120,255, cv2.THRESH_BINARY)

#cv2.blur(img_thresh,(10,10))
#ret, img_thresh = cv2.threshold(img_thresh, 120,255, cv2.THRESH_BINARY)


cv2.imshow('img',img)
cv2.imshow('img_gray',img_gray)
cv2.imshow('img_thresh',img_thresh)


cv2.waitKey(0)
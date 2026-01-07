import os
import cv2

img = cv2.imread(os.path.join('.','data', 'drakemaye.jpg'))


print(img.shape)

cropped_img = img[60:140, 80:170]


cv2.imshow('img',img)
cv2.imshow('cropped_img',cropped_img)
cv2.waitKey(0)
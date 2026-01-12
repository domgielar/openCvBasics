import os
import cv2

img = cv2.imread(os.path.join('.','data','drakemaye.jpg'))

#blurring function averaging surronding pixels
k_size=7
img_blur = cv2.blur(img,(k_size,k_size))

#bell-curve, smoth looking blur, preserves edges beter
img_gaussian = cv2.GaussianBlur(img,(k_size,k_size),3)

#more sharper, for salt and pepper images
img_median = cv2.medianBlur(img,k_size)

cv2.imshow('img',img)
cv2.imshow('img_blur',img_blur)
cv2.imshow('img_gaussian',img_gaussian)
cv2.imshow('img_median',img_median)
cv2.waitKey(0)
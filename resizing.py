import os
import cv2

#readimage
img = cv2.imread(os.path.join('.','data','jaysontatum.png'))
#resizeing the image
resized_img = cv2.resize(img,(120, 180))

#prints the pixel amounts/coordinates
print(img.shape)
print(resized_img.shape)

#shows image in tab
cv2.imshow('img',img)
cv2.imshow('resized_img',resized_img)
cv2.waitKey(0)


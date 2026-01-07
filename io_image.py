import os 
import cv2

#read image
image_path=os.path.join('.','data','drakemaye.jpg')
img = cv2.imread(image_path)

#write image
cv2.imwrite(os.path.join('.','data','drakemaye_out.jpg'), img)

# visualize image
cv2.imshow('image', img)
#wait key will make the window stay open when viewing the image
cv2.waitKey(0)
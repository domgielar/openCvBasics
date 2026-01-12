import os
import cv2

img = cv2.imread(os.path.join('.','data', 'whiteboard.jpg'))
print(img.shape)

#line
cv2.line(img, (40, 80),(80, 120), (0,255,0), 3)

#rectangle

cv2.rectangle(img, (120, 150),(160, 200),(0,0,255),-1)

#circle

cv2.circle(img, (137, 92),30,(255,0,0), 10)


#text

cv2.putText(img, 'Hello, World!', (50, 20), cv2.FONT_HERSHEY_SIMPLEX,1, (255,255,0),2)



cv2.imshow('img', img)
cv2.waitKey(0)
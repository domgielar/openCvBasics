import os
import cv2

img = cv2.imread(os.path.join('.','data','birds.jpg'))
#you have to apply gray scale becuase it needs to be one dimnesional
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh= cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)


contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#how many isolated birds there are
#for cnt in contours:
#   print(cv2.contourArea(cnt))

#drawing outline on original img a green outline
for cnt in contours:
    if cv2.contourArea(cnt)>200:
        #cv2.drawContours(img,cnt,-1,(0,255,0),1)


        #image processing object it draws boxes around objects.
        x1,y1,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),2)


cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)

cv2.waitKey(0)
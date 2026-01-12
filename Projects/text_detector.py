import cv2
import os 
from PIL import Image
import pytesseract

image = "./textdata/motivation.jpeg"
text = pytesseract.image_to_string(Image.open(image), lang='eng')

print(text)
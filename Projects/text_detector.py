import cv2
import os 
from PIL import Image
import pytesseract
from easyocr import Reader
import boto3

image = "./textdata/motivation.jpeg"
text = pytesseract.image_to_string(Image.open(image), lang='eng')

reader = Reader(["en"])

text = ''
results = reader.readtext(image)
for result in results:
    #Since the first coordinate in the array [0] is the position [1] is the value 
    text = text +result[1] + ' '

text = text [:-1]

print(text)




from paddleocr import PaddleOCR, draw_ocr # main OCR dependencies
from matplotlib import pyplot as plt # plot images
import cv2 #opencv
import os

# Setup model
ocr_model = PaddleOCR(lang='en')

img_path = os.path.join('.', 'avi34.jpg')

result = ocr_model.ocr(img_path)

result

for res in result:
    print(res[1][0])

boxes = [res[0] for res in result] # 
texts = [res[1][0] for res in result]
scores=[res[1][1] for res in result]

font_path = os.path.join('PaddleOCR', 'doc', 'fonts', 'latin.ttf')

# imports image
img = cv2.imread(img_path) 

# reorders the color channels
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Visualize our image and detections
# resizing display area
plt.figure(figsize=(15,15))

# draw annotations on image
annotated = draw_ocr(img, boxes, texts,scores, font_path=font_path) 

# show the image using matplotlib
plt.imshow(annotated)
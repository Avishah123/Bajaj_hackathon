import numpy as np
import cv2
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'"C:\Users\getav\Downloads\tesseract-ocr-w64-setup-v5.1.0.20220510.exe"'


import pytesseract
import re

from pytesseract import Output


def plot_gray(image):
    plt.figure(figsize=(16,10))
    return plt.imshow(image, cmap='Greys_r')
def plot_rgb(image):
    plt.figure(figsize=(16,10))
    return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
def text_extraction(file_name):
    
    image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE) 
    plot_gray(image)
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
    n_boxes = len(d['level'])
    boxes = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])    
        boxes = cv2.rectangle(boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    plot_rgb(boxes)
    extracted_text = pytesseract.image_to_string(image)
    print(extracted_text)
    return extracted_text
imgfile_name = "avi2.png" #previously obtained scanned receipt image path
result_text = text_extraction(imgfile_name)
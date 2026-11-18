import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('multiQR.png')

for barcode in decode(img):
    print(barcode.rect)
    print(f"Data ------> {barcode.data.decode('utf-8')}")
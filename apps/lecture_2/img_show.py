import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('cat.bmp')
"""
print(type(img))
print(img.shape)
print(img.dtype)

<class 'numpy.ndarray'>
(480, 640, 3)   # height, width, BGR
uint8
"""

cv.namedWindow('Image')
cv.imshow('Image', img)

while True:
    if cv.waitKey(0) == 27:
        break

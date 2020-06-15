import cv2 as cv

img = cv.imread('files/cat.bmp')
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
    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()

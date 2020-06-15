import sys
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('camera open failed')
    sys.exit()

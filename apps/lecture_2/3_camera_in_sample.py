import sys
import cv2 as cv

cap = cv.VideoCapture('files/small.mp4')

if not cap.isOpened():
    print('Camera open failed')
    sys.exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    edge = cv.Canny(frame, 50, 150)
    cv.imshow('frame', frame)
    cv.imshow('edge', edge)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()

import cv2 as cv
import matplotlib.pyplot as plt

# 컬러영상 출력
img = cv.imread('cat.bmp')
imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv.imread('cat.bmp', cv.IMREAD_GRAYSCALE)
plt.axis('off')
plt.imshow(imgGray, cmap = 'gray')
plt.show()

# 두개의 영상 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap = 'gray')
plt.show()

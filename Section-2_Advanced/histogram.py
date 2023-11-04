import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('benedict.jpg')
cv.imshow('Benedict', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2 - 90), 100, 255, -1)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow("Maksed", masked)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], masked, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# Color Histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], masked, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
    plt.figure()
    plt.title('Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')

plt.show()
cv.waitKey(0)
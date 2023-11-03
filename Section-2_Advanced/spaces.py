import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('benedict.jpg')
cv.imshow('Benedict', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# Gray to BGR
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow("Gray --> BGR", gray_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)
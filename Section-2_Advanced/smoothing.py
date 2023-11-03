import cv2 as cv

img = cv.imread('benedict.jpg')
cv.imshow('Benedict', img)

# Averaging
average = cv.blur(img, (55, 55))
cv.imshow('Averaged blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (55, 55), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 55)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 55, 75, 75)
cv.imshow('Bilateral ', bilateral)

cv.waitKey(0)
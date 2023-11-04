import cv2 as cv
import numpy as np

img = cv.imread('benedict.jpg')
cv.imshow('Benedict', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



cv.waitKey(0)
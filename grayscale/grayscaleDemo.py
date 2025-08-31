import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt

def grayScale():
    img = cv.imread("sunset.jpg")
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("original", img)
    cv.imshow("gray", imgGray)
    cv.waitKey(0)
    
def readAsGray():
    img = cv.imread("sunset.jpg", cv.IMREAD_GRAYSCALE)

    cv.imshow("gray", img)
    cv.waitKey(0)

if __name__ == "__main__":
    # grayScale()
    readAsGray()
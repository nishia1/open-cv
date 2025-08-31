import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt

def hsvColorSegmentation():
    img = cv.imread("sunset.jpg")
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    hsv =cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lowerBound = np.array([0, 50, 50])
    upperBound = np.array([10, 255, 255])
    mask = cv.inRange(hsv, lowerBound, upperBound)
    result = cv.bitwise_and(imgRGB, imgRGB, mask=mask)
    cv.imshow("mask", mask)
    cv.waitKey(0)
    cv.imshow("result", result)
    
    plt.figure(131)
    plt.imshow(imgRGB)
    plt.title('original')
    # plt.figure(132)
    # plt.imshow(hsv)
    # plt.title('hsv')
    plt.show()

if __name__ == "__main__":
    hsvColorSegmentation()
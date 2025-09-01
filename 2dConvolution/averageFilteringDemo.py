import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt

def callback(input):
    pass

def averageFiltering():
    img = cv.imread("sunset.jpg")
    winName = 'avg filter'
    cv.namedWindow(winName)
    cv.createTrackbar('n', winName, 1,100,callback)

    height,width,_ = img.shape
    scale = 1/4
    width = int(width*scale)
    height = int(height*scale)
    img = cv.resize(img, (width,height))

    # gets more and more blurry as n increases since averaging more pixels
    # edges begin to disappear
    while True:
        if cv.waitKey(1) == ord('q'):
            break
        n = cv.getTrackbarPos('n', winName)
        imgFilter = cv.blur(img, (n,n))
        cv.imshow(winName, imgFilter)
    cv.destroyAllWindows()

if __name__ == "__main__":
    averageFiltering()
# needed for smoothing/blurring, feature extracion, image enhancement, nd edge detections
import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt

def convolution2D():
    img = cv.imread("sunset.jpg")
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    n = 100
    # averaging filter
    kernel = np.ones((n,n),np.float32)/(n*n)
    imgFilter = cv.filter2D(imgRGB,-1,kernel)

    plt.figure()
    plt.subplot(121)
    plt.imshow(imgRGB)
    plt.title('original')

    plt.subplot(122)
    plt.imshow(imgFilter)
    plt.title('2D convolution')

    plt.show()


if __name__ == "__main__":
    convolution2D()
# image histogram shows distribution of pixel intensity
# needed for thresholding, equilization, enhancement, color analysis and segmentation
# count # of pixels for each pixel intensity (0-255)
import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt

def grayHistogram():
    img = cv.imread("sunset.jpg", cv.IMREAD_GRAYSCALE)
    
    plt.figure()
    plt.imshow(img, cmap='gray')
    plt.title('gray image')

    hist = cv.calcHist([img], [0], None, [256], [0,256])

    plt.figure()
    plt.plot(hist)
    plt.xlabel("bins")
    plt.ylabel("# of pixels")
    plt.show()

def colorHistogram():
    img = cv.imread("sunset.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.figure()
    plt.imshow(img)
    plt.title('color image')

    colors = ['b', 'g', 'r']
    plt.figure()
    for i in range(len(colors)):
        hist = cv.calcHist([img], [i], None, [256], [0,256])
        plt.plot(hist, colors[i])

    plt.xlabel("pixel intensity")
    plt.ylabel("# of pixels")

    plt.show()

def histogramRegion():
    img = cv.imread("sunset.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgRGB = imgRGB[675:825,600:800,:]

    plt.figure()
    plt.imshow(imgRGB)
    plt.title('color image region')

    colors = ['b', 'g', 'r']
    plt.figure()
    for i in range(len(colors)):
        hist = cv.calcHist([img], [i], None, [256], [0,256])
        plt.plot(hist, colors[i])

    plt.xlabel("pixel intensity")
    plt.ylabel("# of pixels")

    plt.show()

if __name__ == "__main__":
    #grayHistogram() 
    #colorHistogram()
    histogramRegion()
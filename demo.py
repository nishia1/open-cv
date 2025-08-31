import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

# read image & write image

def readImage():
    sunset = cv.imread('sunset.jpg')
    breakpoint()
    cv.imshow('sunset', sunset)
    cv.waitKey(0)

def writeImage():
    img = cv.imread("sunset.jpg")
    outPath = "output.jpg"
    cv.imwrite(outPath, img)


if __name__ == '__main__':
    # readImage()
    writeImage()
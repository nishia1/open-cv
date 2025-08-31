import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

# read image & write image

def readImage():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    imgPath = os.path.join(script_dir, "sunset.jpg")
    sunset = cv.imread(imgPath)
    breakpoint()
    cv.imshow('sunset', sunset)
    cv.waitKey(0)

def writeImage():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    imgPath = os.path.join(script_dir, "sunset.jpg")
    sunset = cv.imread(imgPath)
    outPath = "output.jpg"
    cv.imwrite(outPath, sunset)


if __name__ == '__main__':
    # readImage()
    writeImage()
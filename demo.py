import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def readImage():
    sunset = cv.imread('sunset.jpg')
    breakpoint()
    cv.imshow('sunset', sunset)
    cv.waitKey(0)

if __name__ == '__main__':
    readImage()
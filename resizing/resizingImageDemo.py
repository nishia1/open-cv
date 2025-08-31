import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt

def imageResize():
    img = cv.imread("sunset.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # cropping img
    img = img[500:600,300:400,:]
    height,width,_ = img.shape

    # scale = 1/4
    scale = 4

    # trying various interpolation methods
    interpMethods = [
        cv.INTER_AREA,
        cv.INTER_LINEAR,
        cv.INTER_NEAREST,
        cv.INTER_CUBIC,
        cv.INTER_LANCZOS4
    ]

    interpTitles = ['area','linear','nearest','cubic','lanczos4']

    plt.figure()
    plt.subplot(2,3,1)
    plt.imshow(img)

    for i in range(len(interpMethods)):
        plt.subplot(2,3,i+2)
        imgResize = cv.resize(img,(int(width*scale), int(height*scale)))
        interpolation = interpMethods[i]
        plt.imshow(imgResize)
        plt.title(interpTitles[i])
    plt.show()

if __name__ == "__main__":
    imageResize()
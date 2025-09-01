# median filtering - filtering method that finds median valus within given region
# used for noise reduction & edge preservation
# look within kernel window & replace center pixel with median value
# if nose is salt and pepper noise (0 or 255), choosing median value will always ignore noise
import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt

def medianFiltering():
    img = cv.imread("sunset.jpg")
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    noisyImg = imgRGB.copy()
    noiseProb = 0.05
    noise = np.random.rand(noisyImg.shape[0], noisyImg.shape[1])
    noisyImg[noise<noiseProb/2] = 0
    noisyImg[noise > 1 - noiseProb/2] = 255

    imgFilter = cv.medianBlur(noisyImg, 5)

    plt.figure()
    plt.subplot(131)
    plt.imshow(noisyImg)
    plt.title('noisy image')
    plt.subplot(132)
    plt.imshow(imgFilter)
    plt.title('median filtering')
    plt.show()

if __name__ == "__main__":
    medianFiltering()
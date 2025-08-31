import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def readAndWriteASinglePixel():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    imgPath = os.path.join(script_dir, "sunset.jpg")
    img = cv.imread(imgPath)
    # convert BGR to RGB
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # can see pixel values 
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    # try seeing specific pixel
    imgRGB[312, 350] = (255, 0, 0)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    debug = 1

# access region of the image
def readAndWritePixelRegion():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    imgPath = os.path.join(script_dir, "sunset.jpg")
    img = cv.imread(imgPath)
    
    # convert BGR to RGB
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    # rows, cols
    eyeRegion = imgRGB[230:340, 326:600]

    dx = 340 - 230
    dy = 600 - 326

    startX = 0
    startY = 400

    imgRGB[startX:startX+dx, startY:startY+dy] = eyeRegion

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == '__main__':
    # readAndWriteASinglePixel()
    readAndWritePixelRegion()
import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def pureColors():
    zeros = np.zeros([100,100])
    ones = np.ones([100,100])
    # need to put in RGB format to show correctly due to the way plt works
    # matplotlib uses RGB while OpenCV uses BGR
    # that is why blue channel is in the third dimension opposed to the first dimension
    # red when first run, happens because plt.imshow use RGB and therefore shows in diff order
    # cv doesnt have sub plot feature
    bImg = cv.merge((zeros, zeros, 255*ones))
    gImg = cv.merge((zeros, 255*ones, zeros))
    rImg = cv.merge((255*ones, zeros, zeros))
    # black and white?
    blackImg = cv.merge((zeros, zeros, zeros))
    whiteImg = cv.merge((255*ones, 255*ones, 255*ones))

    plt.figure()
    plt.subplot(231)
    plt.imshow(bImg)
    plt.title('blue')

    plt.subplot(232)
    plt.imshow(gImg)
    plt.title('green')

    plt.subplot(233)
    plt.imshow(rImg)
    plt.title('red')

    plt.subplot(234)
    plt.imshow(blackImg)
    plt.title('black')

    plt.subplot(235)
    plt.imshow(whiteImg)
    plt.title('white')

    plt.show()

def bgrChannelGrayscale():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    imgPath = os.path.join(script_dir, "sunset.jpg")
    img = cv.imread(imgPath)
    b, g, r = cv.split(img)

    plt.figure()
    plt.subplot(131)
    plt.imshow(b, cmap='gray')
    plt.title('b')

    plt.subplot(132)
    plt.imshow(g, cmap='gray')
    plt.title('g')

    plt.subplot(133)
    plt.imshow(r, cmap='gray')
    plt.title('r')

    plt.show()

def bgrChannelColor():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    imgPath = os.path.join(script_dir, "sunset.jpg")
    img = cv.imread(imgPath)
    b, g, r = cv.split(img)
    zeros = np.zeros_like(b)

    bImg = cv.merge((zeros, zeros, b))
    gImg = cv.merge((zeros, g, zeros))
    rImg = cv.merge((r, zeros, zeros))

    plt.figure()
    plt.subplot(131)
    plt.imshow(bImg)
    plt.title('b')
    plt.subplot(132)
    plt.imshow(gImg)
    plt.title('g')
    plt.subplot(133)
    plt.imshow(rImg)
    plt.title('r')
    plt.show()

if __name__ == '__main__':
    #pureColors()
    # bgrChannelGrayscale()
    bgrChannelColor()
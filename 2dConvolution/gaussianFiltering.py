# gaussian filtering - filtering method that uses gaussian kernel for convolution
# used for noise reduction & general preprocessing
# sigma term controls skinny/fat of gaussian kernel
import cv2 as cv
import os
import numpy as np
from matplotlib import pyplot as plt

def callback(input):
    pass

def gaussianKernel(size, sigma):
    kernel = cv.getGaussianKernel(size, sigma)
    kernel = np.outer(kernel, kernel)
    return kernel

def gaussianFiltering():
    img = cv.imread("sunset.jpg")

    n = 51
    fig = plt.figure()
    plt.subplot(121)
    kernel = gaussianKernel(n, sigma=8)
    plt.imshow(kernel)

    ax = fig.add_subplot(122, projection='3d')
    x = np.arange(0,n,1)
    y = np.arange(0,n,1)
    X,Y = np.meshgrid(x,y)
    ax.plot_surface(X, Y, kernel, cmap='viridis')

    plt.show()

    winName = 'gaus filter'
    cv.namedWindow(winName)
    cv.createTrackbar('sigma', winName, 1, 20, callback)
    height, width,_ = img.shape
    scale = 1/2
    width = int(width*scale)
    height = int(height*scale)
    img = cv.resize(img, (width,height))

    # good way to identify correct sigma value for application
    while True:
        if cv.waitKey(1) == ord('q'):
            break
        sigma = cv.getTrackbarPos('sigma', winName)
        imgFilter = cv.GaussianBlur(img, (n,n), sigma)
        cv.imshow(winName, imgFilter)
    cv.destroyAllWindows()

if __name__ == "__main__":
    gaussianFiltering()
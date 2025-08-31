import numpy as np
import cv2 as cv
import os

# vid downloaded from https://www.youtube.com/watch?v=lycJwHNdYug

def videoFromWebcam():
    # only have one webcam, so should be 0
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        exit()
    
    while True:
        ret, frame = cap.read()
        if ret:
            cv.imshow('Webcam', frame)
        
        # wait one millsecond and see if 'q' key is pressed
        if cv.waitKey(1) == ord('q'):
            break
    # release webcam
    cap.release()
    # close all windows
    cv.destroyAllWindows()

def videoFromFile():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    vidPath = os.path.join(script_dir, "puppies.mp4")
    cap = cv.VideoCapture(vidPath)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame")
            break
        cv.imshow("video", frame)
        
        # assuming 60 fps video
        #delay = int(1000/60)
        
        # what if i want to speed it up? trying 2x speed
        #delay = int(1000/120)
        
        # what about slow it down? trying 0.25x speed
        delay = int(1000/15)
        
        if cv.waitKey(delay) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    # videoFromWebcam()
    videoFromFile()
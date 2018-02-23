# OpenCV program to perform Edge detection in real time and translate into transform pixels
# import libraries of python OpenCV
# where its functionality resides
import cv2

# np is an alias pointing to numpy library
import numpy as np


# capture frames from a camera
cap = cv2.VideoCapture(0)


# auto canny using median
def auto_canny(vid, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(vid)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(vid, lower, upper)

    # return the edged image
    return edged


# loop runs if capturing has been initialized
while(1):

    # reads frames from a camera
    ret, frame = cap.read()

    # converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    # create a red HSV colour boundary and
    # threshold HSV image
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # filters
    kernel = np.ones((15,15),np.float32)/225
    filter = cv2.GaussianBlur(frame, (15,15), 0)
    #filter = cv2.medianBlur(filter1,15)
    #filter = cv2.bilateralFilter(filter2,15,75,75)
    #filter = cv2.filter2D(frame,-1,kernel)

    # no filter
    #filter = frame

    # Display an original image
    cv2.imshow('Original',filter)


    # finds edges in the input image image and
    # marks them in the output map edges
    lgEdges = auto_canny(filter)

    # create small image (24x16) and edges
    smFrame = cv2.resize(filter, (24,16), interpolation = cv2.INTER_NEAREST)
    smEdges = auto_canny(smFrame)

    # resize windows
    # large
    cv2.namedWindow('lgEdges',cv2.WINDOW_NORMAL)
    lgEdges = cv2.resize (lgEdges, (480,320), interpolation = cv2.INTER_NEAREST)
    # small
    cv2.namedWindow('smEdges',cv2.WINDOW_NORMAL)
    smEdges = cv2.resize (smEdges, (480,320), interpolation = cv2.INTER_NEAREST)

    # Display edges in a frame
    # large
    cv2.imshow('lgEdges', lgEdges)
    # small
    cv2.imshow('smEdges', smEdges)


    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

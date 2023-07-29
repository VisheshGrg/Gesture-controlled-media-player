import cv2
import numpy as np
def nothing(x):
    pass

def createTrackbar(name,l,u):
    cv2.namedWindow("thresholding")
    cv2.resizeWindow("thresholding",550,80)
    cv2.createTrackbar(name,"thresholding",l,u,nothing)

img = cv2.imread('C:\dip\hand.jpg')
# cv2.imshow("Original Image", img)

gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Scale Image", gray_scale)

createTrackbar("H_min",0,180)
createTrackbar("S_min",0,255)
createTrackbar("V_min",0,255)
createTrackbar("H_max",0,180)
createTrackbar("S_max",0,255)
createTrackbar("V_max",0,255)

while True:
    H_min = cv2.getTrackbarPos("H_min","thresholding")
    S_min = cv2.getTrackbarPos("S_min","thresholding")
    V_min = cv2.getTrackbarPos("V_min","thresholding")
    H_max = cv2.getTrackbarPos("H_max","thresholding")
    S_max = cv2.getTrackbarPos("S_max","thresholding")
    V_max = cv2.getTrackbarPos("V_max","thresholding")
    
    # print(T)
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([H_min,S_min,V_min])
    upper = np.array([H_max,S_max,V_max])
    thresh_img = cv2.inRange(img_hsv,lower,upper)
    cv2.imshow("Threshold Image", thresh_img)

    img_copy = img.copy()
    contours,_ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(contours)
    cv2.drawContours(img_copy, contours, -1, (255,0,0), 2)
    cv2.imshow("Contour image", img_copy)

    key = cv2.waitKey(1)
    if(key==ord('q')):
        break   

cv2.waitKey(0)
cv2.destroyAllWindows()
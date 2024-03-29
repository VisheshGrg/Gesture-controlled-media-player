import cv2
import numpy as np
import time
import pyautogui

MOTION_UP = "Up"
MOTION_DOWN = "Down"
MOTION_LEFT = "Left"
MOTION_RIGHT = "Right"
NO_MOTION = "_"


def empty(a):
    pass

def create_trackbars():
    cv2.namedWindow('Trackbars')
    cv2.resizeWindow('Trackbars', 640, 300)
    cv2.createTrackbar('HueMin', 'Trackbars', 0, 179, empty)
    cv2.createTrackbar('HueMax', 'Trackbars', 179, 179, empty)
    cv2.createTrackbar('SatMin', 'Trackbars', 100, 255, empty)
    cv2.createTrackbar('SatMax', 'Trackbars', 235, 255, empty)
    cv2.createTrackbar('ValMin', 'Trackbars', 185, 255, empty)
    cv2.createTrackbar('ValMax', 'Trackbars', 255, 255, empty)

def create_mask(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_min = cv2.getTrackbarPos('HueMin', 'Trackbars')
    hue_max = cv2.getTrackbarPos('HueMax', 'Trackbars')
    sat_min = cv2.getTrackbarPos('SatMin', 'Trackbars')
    sat_max = cv2.getTrackbarPos('SatMax', 'Trackbars')
    val_min = cv2.getTrackbarPos('ValMin', 'Trackbars')
    val_max = cv2.getTrackbarPos('ValMax', 'Trackbars')
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    return mask

def find_contours(thresh):
    contours, heirarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)  #give list of all essential boundary points
    return contours

def max_contour(contours):
    if len(contours) == 0:
        return []
    max_cntr = max(contours, key=lambda x: cv2.contourArea(x))
    epsilon = 0.005 * cv2.arcLength(
        max_cntr, True
    )  # maximum distance from contour to approximated contour. It is an accuracy parameter
    max_cntr = cv2.approxPolyDP(max_cntr, epsilon, True)
    return max_cntr

def threshold(mask):
    _, thresh = cv2.threshold(
        mask, 127, 255, cv2.THRESH_BINARY
    )  # if pixel intensity <= 127 then set it as 0 and pixel intensity > 127 set it as 255
    return thresh

def centroid(cnt):
    if(len(cnt) == 0):
        return (-1,-1)
    
    M = cv2.moments(cnt)

    try:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
    except ZeroDivisionError:
        return (-1,-1)

    return (x,y)    

def clean_image(mask):
    img_eroded = cv2.erode(mask,(3,3), iterations=1)  
    img_dilated = cv2.dilate(img_eroded,(3,3),iterations = 1)
    return img_dilated

def detect_hand(mask):
    return np.average(mask) > 50

def velocity(x1,x2,t):
    return (x2 - x1)/t

def detect_motion(x1,y1,x2,y2,t):
    vel_x = int(velocity(x1,x2,t))
    vel_y = int(velocity(y1,y2,t))
    # print("The velocity of x is ",vel_x)
    if vel_x > 25:
        # print("Hello")
        return MOTION_RIGHT
    elif vel_x < -25:
        return MOTION_LEFT
    elif vel_y > 20:
        return MOTION_DOWN
    elif vel_y < -20:
        return MOTION_UP
    else:
        return NO_MOTION

# performing actions based on hand motion
def performAction(hand_motion):
    if hand_motion == MOTION_RIGHT:
        pyautogui.press('right')
    elif hand_motion == MOTION_LEFT:
        pyautogui.press('left')
    elif hand_motion == MOTION_UP:
        pyautogui.press('up')
    elif hand_motion == MOTION_DOWN:
        pyautogui.press('down')


#################################################################################
########## Driver Code ##########################################################
#################################################################################

vid = cv2.VideoCapture(0)
create_trackbars()

prev_x, prev_y, cu_x, cur_y = -1,-1,-1,-1
frame_num = 4
last_timestamp = 0
lastMotion = False;

while True:   
    _, frame = vid.read()
    frame = cv2.flip(frame, 1)  # resolving mirror image issues
    # it is used to flip the image so that it is not inverted

    # Cropping the frame so that only right-half frame will detect hand motion
    height, width = frame.shape[:2]

        # Let's get the starting pixel coordiantes (top left of frame)
    start_row, start_col = int(0), int(width * .5)
    # Let's get the ending pixel coordinates (bottom right of frame)
    end_row, end_col = int(height), int(width)

    frame = frame[
        start_row:end_row, start_col:
        end_col]  # only considering frame row from start_row to end_row and col from start_col to end_col, so that main focus is on our hands

    frame = cv2.GaussianBlur(frame, (5, 5), 0)  # to remove noise from frame (both the numbers should be same)

    mask = create_mask(frame)
    threshImg = threshold(mask)
    contours = find_contours(mask)
    frame = cv2.drawContours(frame, contours, -1, (255, 0, 0),
                             2)  # drawing all contours
    max_cntr = max_contour(
        contours)  # finding maximum contour of the thresholded area

    (centroid_x, centroid_y) = centroid(max_cntr)
    if(centroid_x !=-1 and centroid_y != -1):
        frame = cv2.circle(frame, (centroid_x,centroid_y), 5,(255,255,0), -1)
        # print(centroid_x, centroid_y)
        # print(cv2.contourArea(max_cntr))
        hand_detected = cv2.contourArea(max_cntr) >=2000
        if hand_detected:
            if lastMotion==True:
                pyautogui.press("space")
                lastMotion = False  
            if prev_x == -1:
                prev_x, prev_y = centroid_x, centroid_y
                frame_num = 4                                 
                # print(prev_x,prev_y)
            if frame_num == 0:

                cur_time = time.time()
                time_elapsed = cur_time - last_timestamp
                hand_motion = detect_motion(prev_x, prev_y, 
                        centroid_x, centroid_y, time_elapsed)
                print(hand_motion)
                performAction(hand_motion)
                prev_x, prev_y = centroid_x, centroid_y
                last_timestamp = time.time()

                # Re-initializing the frame counter
                if hand_motion != NO_MOTION:
                    frame_num = 4
                else:
                    frame_num = 8
            else:
                frame_num -= 1

        else:
            if lastMotion == False:
                pyautogui.press("space")
                lastMotion = True
            prev_x, prev_y = -1, -1
            frame_num = 4

    print(lastMotion)
    cv2.imshow('video', frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(10)

    if key == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()

import cv2
import numpy as np
import random

img_path = "C:\dip\sherlock_kid.png";
img = cv2.imread(img_path)

img_copy = np.full((400,760,3),(random.randint(0,256),random.randint(0,256),random.randint(0,256)),dtype=np.uint8)
# img_copy = np.full((600,600,200),(random.randint(0,256),random.randint(0,256),random.randint(0,256)),dtype=np.uint8)
netImage = np.subtract(img_copy,img)
cv2.imshow("Net Image", netImage)

key = cv2.waitKey(10000)
if key==ord('d'):
    cv2.imwrite("C:\dip\SavedImg.png", netImage)

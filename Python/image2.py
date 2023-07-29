import cv2
import numpy as np

img_path = "C:\dip\sherlock_kid.png"
img = cv2.imread(img_path)

img_copy = np.full((400,760,3),(0,0,50),dtype=np.uint8)
netImage = np.add(img_copy,img)
cv2.imshow("Net Image", netImage)

cv2.waitKey(0)
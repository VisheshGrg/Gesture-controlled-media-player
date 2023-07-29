import cv2

img_path = "C:\dip\sherlock_kid.png"
img = cv2.imread(img_path)
# print(img.shape)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGBA)
cv2.imshow("Image",img)
# cv2.imshow("Gray Image",img_gray)
# cv2.imshow("HSV Image", img_hsv)
# cv2.imshow("RGB Image", img_rgb)
# cv2.waitKey(2000)
# for indefinte time
#to download a image
cv2.imwrite("C:\dip\sherlock_kid_gray.png", img_gray)
img_resized = cv2.resize(img, (600,500))
# cv2.imshow("Resized Image", img_resized)

img_sliced = img[:,350:700]
cv2.imshow("Image Sliced", img_sliced)
cv2.waitKey(0)




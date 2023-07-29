import cv2

img_path = 'C:/dip/book_page.jpg'
img = cv2.imread(img_path)
gray_scale_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)

# thresh_val,thresh_img = cv2.threshold(gray_scale_img,127,255,cv2.THRESH_BINARY)
thresh_val,thresh_img = cv2.threshold(gray_scale_img,127,255,cv2.THRESH_OTSU)
cv2.imshow("Binary Image", thresh_img)

# (h,w) = gray_scale_img.shape
# def Thresh(img, threshold_value):
#     for i in range(0,h):
#         for j in range(0,w):
#             if gray_scale_img[i][j] > threshold_value:
#                 gray_scale_img[i][j] = 255
#             else:
#                 gray_scale_img[i][j] = 0

# Thresh(gray_scale_img,120)
# cv2.imshow("Binary Image", gray_scale_img)

cv2.waitKey(0)
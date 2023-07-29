import cv2

video_reader = cv2.VideoCapture(0)   #REadin from webcam

while True:
    success, frame = video_reader.read()
    if not success:
        break 

    cv2.imshow("My vedio", frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break 

video_reader.release()
cv2.destroyAllWindows()
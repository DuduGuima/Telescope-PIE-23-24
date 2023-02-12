import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cam.set(cv2.CAP_PROP_FOCUS, 30)
cam.set(cv2.CAP_PROP_FPS, 50)

ret, image = cam.read()
#cv2.imshow('Imagetest',image)

cv2.imwrite('images/test.jpg', image)
cam.release()
cv2.destroyAllWindows()
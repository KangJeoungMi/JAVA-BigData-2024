# file : p61_opencv.py
# desc : openCV 계속

# OpenCV 실시간 이미지 프로세싱 라이브러리

import cv2

image = cv2.imread('./DAY09/CAT.jpg',cv2.IMREAD_UNCHANGED)  
dst = cv2.blur(image, (5,5),anchor=(-1,-1),borderType=cv2.BORDER_DEFAULT)

height, width, channel = image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(image, 100, 255)

cv2.imshow("sobel", sobel) # 입체감 있는 윤곽
cv2.imshow("laplacian", laplacian) # 일반적인 윤곽
cv2.imshow("canny", canny) # 흑백으로 윤곽


cv2.imshow('cat',image) # 원본
cv2.imshow('blur cat',dst) # 블러



cv2.waitKey(0)
cv2.destroyAllWindows()

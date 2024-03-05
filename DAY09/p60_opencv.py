# file : p60_opencv.py
# desc : openCV 이미지 처리 계속

# OpenCV 실시간 이미지 프로세싱 라이브러리

import cv2

image = cv2.imread('./DAY09/CAT.jpg',cv2.IMREAD_UNCHANGED)  
dst = cv2.flip(image,0) #  0 : 상하반전, 1 : 좌우반전


height, width, channel = image.shape
matrix = cv2.getRotationMatrix2D((width/2,height/2),90, 1) # ccw : 반시계 방향, cw : 시계방향, 2이상(배율)
thrd = cv2.warpAffine(image,matrix,(width,height))

reverse = cv2.bitwise_not(image) # 역상 반전색
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('cat',image)
cv2.imshow('Flip cat',dst)
cv2.imshow('rotate cat', thrd)
cv2.imshow('reverse cat', reverse)
cv2.imshow('gray cat', gray)
cv2.imshow('ret cat', ret)
cv2.imshow('bny cat', bny)

cv2.waitKey(0)
cv2.destroyAllWindows()


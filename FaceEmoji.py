import cv2 , numpy

#to create black box
img = numpy.zeros((700,700,3))

#left eye - two rectangles and circle
img = cv2.rectangle(img , (150,150),(300,300),[0,255,0],5)
img = cv2.rectangle(img , (190,190),(260,260),[0,255,0],5)
img = cv2.circle(img, (225,230), 15, [213,124,12], 5)

#right eye - two rectangles and circle
img = cv2.rectangle(img , (550,150),(400,300),[0,255,60],5)
img = cv2.rectangle(img , (440,190),(510,260),[0,255,0],5)
img = cv2.circle(img, (475,230), 15, [213,124,12], 5)

#mouth 
img = cv2.rectangle(img , (250,550),(450,500),[255,255,0],5)

#nose
img = cv2.circle(img, (350,350), 55, [213,124,12], 5)
#outside circle
img = cv2.circle(img, (350,350), 300, [213,124,12], 5)

cv2.imshow("hii" , img)
cv2.waitKey()
cv2.destroyAllWindows()
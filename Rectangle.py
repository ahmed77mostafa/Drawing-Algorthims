import cv2
import numpy

image = numpy.ones((300,300,3), dtype = numpy.uint8) * 255

start_point = (100,100)
end_point = (200,200)
color = (0,255,0)

cv2.rectangle(image, start_point, end_point, color, -1)
scaled_image = cv2.resize(image, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_LINEAR)

cv2.imshow('Original Rectangle', image)
cv2.imshow('Scaled Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
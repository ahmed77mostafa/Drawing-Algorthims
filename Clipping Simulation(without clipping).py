import cv2
import numpy

image = numpy.ones((400,400,3), dtype = numpy.uint8) * 255

start_point = (100,100)
end_point = (300,300)
color = (0,255,0)

cv2.rectangle(image, start_point, end_point, color, 2)

#Clipping Simulation

#1. Drawing Lines without clipping
cv2.line(image,(50,50), (350,350), (255,0,0), 2)
cv2.line(image,(150,50), (150,350), (0,0,255), 2)

cv2.imshow('Clipping Simulation (without clipping)', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
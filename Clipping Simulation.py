import cv2
import numpy

image = numpy.ones((400,400,3), dtype = numpy.uint8) * 255

start_point = (100,100)
end_point = (300,300)
color = (0,255,0)

cv2.rectangle(image, start_point, end_point, color, 2)

#Clipping Simulation

#2. Drawing Lines

x_min, y_min = 100,100
x_max, y_max = 300,300

x1, y1 = 50, 50
x2, y2 = 350, 350
if x1 < x_min: x1 = x_min
if x2 > x_max: x2 = x_max
if y1 < y_min: y1 = y_min
if y2 > y_max: y2 = y_max
cv2.line(image, (x1,y1), (x2,y2), (255,0,0), 2)

x1, y1 = 150, 50
x2, y2 = 150, 350
if x1 < x_min: x1 = x_min
if x2 > x_max: x2 = x_max
if y1 < y_min: y1 = y_min
if y2 > y_max: y2 = y_max
cv2.line(image, (x1,y1),(x2,y2), (0,0,255),2)

cv2.imshow('Clipping Simulation', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
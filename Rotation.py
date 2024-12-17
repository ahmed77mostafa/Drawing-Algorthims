import cv2
import numpy

image = numpy.ones((300,300,3), dtype = numpy.uint8) * 255

start_point = (100,100)
end_point = (200,200)
color = (0,255,0)
cv2.rectangle(image, start_point, end_point, color, -1)

center = (image.shape[0] // 2, image.shape[1] // 2)
rows,cols = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_img = cv2.warpAffine(image,rotation_matrix,(rows,cols))

cv2.imshow('Original Rectangle', image)
cv2.imshow('Rotated Rectangle', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
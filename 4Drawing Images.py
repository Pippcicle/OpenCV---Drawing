import cv2
import numpy as np

image = np.zeros((512,512,3),np.uint8)
cv2.imshow("image", image)
cv2.waitKey(0)

#drawing a circle
centre = (250,250)
radius = 60
colour = (255,255,255)
thickness = 3
circle = cv2.circle(image, centre,radius,colour,thickness)
cv2.imshow("circle", circle)
cv2.waitKey(0)

#drawing a rectangle
startingpoint = (300,300)
endingpoint = (400,400)
colour = (204,255,153)
thickness = 3

#if thickness = -1 it fills in the shape

rectangle = cv2.rectangle(image, startingpoint, endingpoint, colour,thickness)
cv2.imshow("rectangle", rectangle)
cv2.waitKey(0)

#drawing a line
start = (20,20)
end = (50,50)
colour = (153,255,153)
thickness = 3

line = cv2.line(image, start, end, colour, thickness)
cv2.imshow("line", line)
cv2.waitKey(0)

#writing on images
font = cv2.FONT_HERSHEY_PLAIN
origin = (150,150)
fontscaling = 1
colour = (153,153,255)
thickness = 3
text = cv2.putText(image, "Hello!", origin, font, fontscaling, colour, thickness)
cv2.imshow("text", line)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
image = np.zeros((500,500,3), np.uint8)

cv2.imshow("image",image)

start = (250,50)
end = (277,197)
thickness = 3
colour = (0,223,255)
one = cv2.line(image,start,end,colour,thickness)

start = (277,197)
end = (425,197)
thickness = 3
colour = (0,223,255)
two = cv2.line(image,start,end,colour,thickness)

start = (425,197)
end = (300,293)
thickness = 3
colour = (0,223,255)
three = cv2.line(image,start,end,colour,thickness)

start = (300,293)
end = (350,450)
thickness = 3
colour = (0,223,255)
four = cv2.line(image,start,end,colour,thickness)

start = (350,450)
end = (250,350)
thickness = 3
colour = (0,223,255)
five = cv2.line(image,start,end,colour,thickness)

start = (250,350)
end = (150,450)
thickness = 3
colour = (0,223,255)
six = cv2.line(image,start,end,colour,thickness)

start = (150,450)
end = (200,293)
thickness = 3
colour = (0,223,255)
seven = cv2.line(image,start,end,colour,thickness)



start = (200,293)
end = (75,197)
thickness = 3
colour = (0,223,255)
eight = cv2.line(image,start,end,colour,thickness)

start = (75,197)
end = (223,197)
thickness = 3
colour = (0,223,255)
nine = cv2.line(image,start,end,colour,thickness)

start = (223,197)
end = (250,50)
thickness = 3
colour = (0,223,255)
ten = cv2.line(image,start,end,colour,thickness)

cv2.imshow("star",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
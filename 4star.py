import cv2
import numpy as np
image = np.zeros((500,500,3), np.uint8)

cv2.imshow("image",image)

start = (250,10)
end = (320,185)
thickness = 3
colour = (255,213,0)
one = cv2.line(image,start,end,colour,thickness)

start = (320,185)
end = (80,415)
thickness = 3
colour = (255,213,0)
two = cv2.line(image,start,end,colour,thickness)

start = (80,415)
end = (195,290)
thickness = 3
colour = (255,213,0)
three = cv2.line(image,start,end,colour,thickness)

start = (195,290)
end = (420,415)
thickness = 3
colour = (255,213,0)
four = cv2.line(image,start,end,colour,thickness)

start = (420,415)
end = (305,290)
thickness = 3
colour = (255,213,0)
five = cv2.line(image,start,end,colour,thickness)


cv2.imshow("star",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
image = np.zeros((500,500,3), np.uint8)

cv2.imshow("image",image)



start = (250,50)
end = (200,100)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

start = (200,100)
end = (220,100)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

start = (220,100)
end = (180,160)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

start = (180,160)
end = (200,160)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

start = (200,160)
end = (160,220)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

start = (160,220)
end = (340,220)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

start = (340,220)
end = (300,160)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

start = (300,160)
end = (320,160)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

start = (320,160)
end = (290,100)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

start = (290,100)
end = (310,100)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

start = (310,100)
end = (250,50)
thickness = 3
colour = (0,100,0)
line = cv2.line(image,start,end,colour,thickness)

startingpoint = (230,220)
endingpoint = (270,250)
colour = (83,105,131)
thickness = -1
stump = cv2.rectangle(image,startingpoint,endingpoint,colour,thickness)

cv2.imshow("tree",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
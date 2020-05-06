#!/usr/bin/env python
import numpy as np
import cv2
cv2.namedWindow("preview")

# Create a black image
w=1280
h=768
img = np.zeros((h,w,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
rows=20
width=1
for row1 in range(rows):
    for row2 in range(rows):
        r1 = round(row1*(h/rows))
        r2 = round(row2*(h/rows))
        cv2.line(img,(0, r1),(w-1,r2),(255,255,255),width)
        cv2.line(img,(w-1, r1),(0,r2),(255,255,255),width)

cv2.imshow("preview",img)
cv2.waitKey()

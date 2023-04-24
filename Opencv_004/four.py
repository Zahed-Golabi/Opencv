import numpy as np
import cv2


src = cv2.imread("../imgs/logo.png")
cv2.imshow("Opencv Logo", src)
cv2.waitKey(0)
# src shape
h, w, ch = src.shape
print(f"h:{h}, w:{w}, ch:{ch}")

output = src.copy()
for row in range(h):
    for column in range(w):
        b, g, r = src[row, column]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        output[row, column] = [b, g, r]

cv2.imshow("Formatted", output)
cv2.waitKey(0)

cv2.imwrite("formatted.png", output)

import cv2

image = cv2.imread("logo.png")
print(image.shape)
cv2.imshow("Input", image)
cv2.waitKey(0)





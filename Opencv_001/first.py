import cv2

image = cv2.imread("logo.png")
cv2.imshow("Input Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()




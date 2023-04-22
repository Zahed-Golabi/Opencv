import cv2

image = cv2.imread("../imgs/logo.png")
# cv2.namedWindow("Input", cv2.WINDOW_AUTOSIZE)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.png", gray)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# read flower1
flower1 = cv2.imread("../Opencv_005/flower1.png")
cv2.imshow("flower1", flower1)
# JET COLORMAP
dst = cv2.applyColorMap(flower1, cv2.COLORMAP_JET)
cv2.imshow("JET", dst)

# read flower2
flower2 = cv2.imread("../Opencv_005/flower2.png")
cv2.imshow("flower2", flower2)
# MAGMA COLORMAP
dst = cv2.applyColorMap(flower2, cv2.COLORMAP_MAGMA)
cv2.imshow("MAGMA", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

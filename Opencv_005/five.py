import numpy as np
import cv2


flower1 = cv2.imread("./flower1.png")
cv2.imshow("Flower 1", flower1)
# cv2.waitKey(0)

flower2 = cv2.imread("./flower2.png")
cv2.imshow("Flower 2", flower2)
# cv2.waitKey(0)

h, w, ch = flower1.shape
print(f"h: {h}, w: {w}, ch: {ch}")

# Add Flowers
add_result = np.zeros(flower1.shape, flower1.dtype)
cv2.add(flower1, flower2, add_result)
cv2.imshow("Add Flowers", add_result)
# cv2.waitKey(0)

# Subtract Flowers
sub_result = np.zeros(flower1.shape, flower1.dtype)
cv2.subtract(flower1, flower2, sub_result)
cv2.imshow("Subtract Flowers", sub_result)
# cv2.waitKey(0)

# Multiply Flowers
mul_result = np.zeros(flower1.shape, flower1.dtype)
cv2.multiply(flower1, flower2, mul_result)
cv2.imshow("Multiply Flowers", mul_result)
# cv2.waitKey(0)

# Divide Flowers
div_result = np.zeros(flower1.shape, flower1.dtype)
cv2.divide(flower1, flower2, div_result)
cv2.imshow("Divide Flowers", div_result)


cv2.waitKey(0)
cv2.destroyAllWindows()

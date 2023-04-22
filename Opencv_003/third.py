import cv2
import numpy as np

src = cv2.imread("../imgs/logo.png")
cv2.imshow("Input", src)
cv2.waitKey(0)

# change pixel values
image_copy1 = src[:]
image_copy1[100:300, 200:450, :] = 0x000000
cv2.imwrite("./output/image_copy1.png", image_copy1)

# black image
black_image = np.zeros(src.shape, src.dtype)
cv2.imwrite("./output/black_image.png", black_image)

# white image
white_image = np.ones(src.shape, src.dtype) * 255
cv2.imwrite("./output/white_image.png", white_image)

# gray image
gray_image = np.zeros(src.shape, np.uint8)
gray_image[:, :, :] = 127
cv2.imwrite("./output/gray_image.png", gray_image)

# blue image
blue_image = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
blue_image[:, :, 0] = 255
cv2.imwrite("./output/blue_image.png", blue_image)

# green image
green_image = np.zeros((512, 512, 3))
green_image[:, :, 1] = 255
cv2.imwrite("./output/green_image.png", green_image)

# red image
red_image = np.ones(shape=[512, 512, 3], dtype=np.uint8)
red_image[:, :, 2] = 255
cv2.imwrite("./output/red_image.png", red_image)

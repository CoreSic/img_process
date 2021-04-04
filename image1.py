import cv2
import numpy as np

# 读入图片：默认彩色图，cv2.IMREAD_GRAYSCALE灰度图，cv2.IMREAD_UNCHANGED包含alpha通道
img = cv2.imread('img.png')
print(img.shape)
print(type(img))
# 图片显示
cv2.imshow('image1',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()


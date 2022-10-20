import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os.path
# 读取图片
img_path = "photo2.png"
img = Image.open(img_path)

# 图像转化为numpy数组
img = np.asarray(img)
flat = img.flatten()

# 创建直方图函数
def get_histogram(image, bins):
    # 初始化数组并设置元素值为0
    histogram = np.zeros(bins)
    # 循环遍历像素并对像素计数求和
    for pixel in image:
        histogram[pixel] += 1
    # 返回最终结果
    return histogram

# 执行直方图函数
hist = get_histogram(flat, 256)

# 数组展平并计算元素累计和
cs = np.cumsum(hist)

# numerator & denomenator
nj = (cs - cs.min()) * 255
N = cs.max() - cs.min()

# 重新标准化累计和
cs = nj / N

# 由于我们不能在图像中使用浮点值，因此将其转换为uint8
cs = cs.astype('uint8')

# 从flat中每个索引的累加和中获取值，并将其设置为img_new
img_new = cs[flat]

# 把数组放回原来的形状，因为我们将其扁平化了
img_new = np.reshape(img_new, img.shape)

# 设置并排图像显示
fig = plt.figure()
fig.set_figheight(15)
fig.set_figwidth(15)

# 显示真实图像
fig.add_subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original image")

# 显示新图像
fig.add_subplot(1, 2, 2)
plt.imshow(img_new, cmap='gray')
plt.title("Image after contrast adjustment")
filename = os.path.basename(img_path)

plt.show()
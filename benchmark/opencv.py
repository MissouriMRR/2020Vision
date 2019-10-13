"""
Speed benchmark for cpu and gpu versions of opencv.
"""
from timeit import timeit

import numpy as np
import cv2


def convolve(img, kernel_size):
	"""
	Run convolution with opencv.

	Parameters	
	----------
	img: ndarray
		Image to process.
	kernel_size: tuple[int]
		Kernel shape.

	Returns
	-------
	Processed image.
	"""	

	img = cv2.GaussianBlur(img, kernel_size, 0)

	return img


if __name__ == '__main__':
	# print(cv2.getBuildInformation())
	img_shape = (12000, 1200, 3)  # 1.4M pixels
	img_size = img_shape[0] * img_shape[1] * img_shape[2]
	img = np.random.normal(size=img_size).reshape(img_shape)

	kernel = (31, 31)
	gpu_img = cv2.UMat(img)
	cpu_time = timeit(lambda : convolve(img, kernel), number=4)
	print("Moving to GPU")
	gpu_time = timeit(lambda : convolve(gpu_img, kernel), number=8)

	print("CPU time: {0}, GPU time: {1}".format(cpu_time, gpu_time))


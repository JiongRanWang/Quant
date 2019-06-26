# Numpy 数组和普通列表的操作方式也是不同的，Numpy 通过广播机制作用于每一个内部元素，是一种并行化执行的思想，普通list则作用于整体
import numpy as np 

np_list = np.ones(5) * 3
#print(np_list)

normal_list = [1,1,1,1,1] * 3
#print(normal_list)


import numpy as np 

np.zeros(100)

# three rows and two columns
np.zeros((3,2))
np.ones((3,2))

#shape: x = 2, y = 3, z = 3 with random values
np.empty((2,3,3))

np_list = np.ones(5) * 3
#same shape with np_list, but all of values are 0
np.zeros_like(np_list)
#same shape with np_list, but all of values are 1
np.ones_like(np_list)

#Identical matrix
np.eye(3)

#transfer list to np array
data = [[1,2,3,4],[5,6,7,8]]
arr_np = np.array(data)
#print(arr_np)

np.linspace(0,1,10)


# 200 stocks
stock_cnt = 200
# 504 trading day
view_days = 504
#generating a series following standard normal distribution
stock_day_change = np.random.standard_normal((stock_cnt,view_days))

#print(stock_day_change.shape)
#print(stock_day_change[0:2,:5])
#print(stock_day_change[-2:,-5:])

#交换两组股票交易日的切片数据，需要使用copy(),因为numpy内部实现的机制全部是引用操作，所以当不实用copy()的时候得出的结果将会丢失stock_day_change[0:2,0:5]
tmp = stock_day_change[0:2,0:5].copy()
stock_day_change[0:2,0:5] = stock_day_change[-2:,-5:]
stock_day_change[-2:,-5:] = tmp
#print(stock_day_change[0:2,0:5])
#print(stock_day_change[-2:,-5:])

#stock_day_change[0:2,0:5].astype(int)
#np.around(stock_day_change[0:2,0:5],2)

tmp_test = stock_day_change[0:2,0:5].copy()
tmp_test[0][0] = np.nan
#print(tmp_test)
tmp_test = np.nan_to_num(tmp_test) #replace nan with 0
#print(tmp_test)

mask = stock_day_change[0:2,0:5] > 0.5
#print(mask)
tmp_test = stock_day_change[0:2,0:5].copy()
#print(tmp_test[mask])
#print(tmp_test[tmp_test > 0.5])
tmp_test = stock_day_change[-2:,-5:].copy()
# |, & (or, and)
#print(tmp_test[(tmp_test > 1) | (tmp_test < -1)])

# np.all 判断序列中的所有元素是否全部是true， 即对bool序列进行与操作
# np.any 判断序列中是否有元素为true
np.all(stock_day_change[0:2,0:5] > 0)
np.any(stock_day_change[0:2,0:5] > 0)

# 对两个序列对应的元素两两比较，maximum（） 结果集取大，相对使用minimum（） 为取小的结果集
np.maximum(stock_day_change[0:2,0:5],stock_day_change[-2:,-5:])

#序列中数值值唯一且不重复的值组成新的序列
change_int = stock_day_change[0:2,0:5].astype(int)
np.unique(change_int)

# axis = 1
a = np.diff(stock_day_change[0:2,0:5])  #后面的值减去前面的值
#print(a)

#axis = 0
b = np.diff(stock_day_change[0:2,0:5], axis = 0)  #下面对应的值减去上面的值
#print(b)

tmp_test = stock_day_change[-2:,-5:]
a = np.where(tmp_test > 0.5, 1 , 0)
#print(a)
b = np.where(tmp_test > 0.5, 1, tmp_test)
#print(b)
c = np.where(np.logical_and(tmp_test > 0.5, tmp_test < 1),1,0)
#print(c)
d = np.where(np.logocal_or(tmp_test > 0.5, tmp_test < -0.5),1,0)
#print(d)


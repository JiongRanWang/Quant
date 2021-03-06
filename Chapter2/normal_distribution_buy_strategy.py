import numpy as np 
import matplotlib.pyplot as plt 
stock_day_change = np.random.standard_normal((200,504))

keep_days = 50
stock_day_change_test = stock_day_change[:200,0:504 - keep_days]
print(np.sort(np.sum(stock_day_change_test,axis = 1))[:3])
# np.argsort() 将展示排序的原序列号
stock_lower_array = np.argsort(np.sum(stock_day_change_test,axis = 1))[:3]

def show_buy_lower(stock_ind):
    """
    :param stock_ind: 股票序号，即在stock_day_change中的位置
    :return:
    """
    _, axs = plt.subplots(nrows = 1, ncols = 2, figsize = (16,5))
    axs[0].plot(np.arange(0, 504 - keep_days),stock_day_change_test[stock_ind].cumsum())
    cs_buy = stock_day_change[stock_ind][504 - keep_days : 504].cumsum()
    axs[1].plot(np.arange(504 - keep_days, 504),cs_buy)
    return cs_buy[-1]

profit = 0
for stock_ind in stock_lower_array:
    profit += show_buy_lower(stock_ind)
print('买入第{}只股票，从第454个交易日开始持有盈亏:{:.2f}%'.format(stock_lower_array,profit))

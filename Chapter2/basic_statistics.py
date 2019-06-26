import numpy as np 
stock_day_change = np.random.standard_normal((200,504))
stock_day_change_four = stock_day_change[:4,:4]

#横向地分析出某只股票在4天内的统计信息，需要使用参数 axis = 1
#如果想纵向地统计数据，即针对某一个交易日的4只股票进行统计分析，需要使用参数 axis = 0
print('最大涨幅: {}',format(np.max(stock_day_change_four,axis = 1)))
print('最大跌幅: {}',format(np.min(stock_day_change_four,axis = 1)))
print('振幅幅度: {}',format(np.std(stock_day_change_four,axis = 1)))
print('平均涨跌: {}',format(np.mean(stock_day_change_four,axis = 1)))
print('最大涨幅股票: {}'.format(np.argmax(stock_day_change_four,axis = 0)))
print('最大跌幅股票: {}'.format(np.argmin(stock_day_change_four,axis = 0)))

import matplotlib.pyplot as plt 
import scipy.stats as scs

stock_mean = stock_day_change[0].mean()
stock_std = stock_day_change[0].std()
plt.hist(stock_day_change[0],bins = 50, normed=True)
fit_linspace = np.linspace(stock_day_change[0].min(),stock_day_change[0].max())
pdf = scs.norm(stock_mean, stock_std).pdf(fit_linspace)
plt.plot(fit_linspace,pdf,lw = 2, c = 'r')
plt.show()
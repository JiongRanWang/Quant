import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt  

stock_day_change = np.random.standard_normal((200,504))
#print(pd.DataFrame(stock_day_change).head())
#print(pd.DataFrame(stock_day_change).head(5))
#print(pd.DataFrame(stock_day_change)[:5])

#行索引
stock_symbols = ['stock ' + str(x) for x in range(0,stock_day_change.shape[0])]
#print(pd.DataFrame(stock_day_change,index = stock_symbols).head(2))

#列索引
days = pd.date_range('2017-1-1',periods=stock_day_change.shape[1],freq='1d')
df = pd.DataFrame(stock_day_change,index = stock_symbols, columns = days)
#print(df.head(2))

#transpose
df = df.T
#print(df.head())

#以下代码对df进行重新采样，以21天为周期，对21天内的时间求平均来重新塑造数据
df_20 = df.resample('21D',how = 'mean')
#print(df_20.head())

df_stock0 = df['stock 0']
#print(type(df_stock0))   Series
#print(df_stock0.head())
#df_stock0.cumsum().plot()
#plt.show()

df_stock0_5 = df_stock0.cumsum().resample('5D',how = 'ohlc')
df_stock0_20 = df_stock0.cumsum().resample('21D',how = 'ohlc')
#print(df_stock0_5.head())
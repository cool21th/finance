import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas_datareader import data as web
import datetime


start = datetime.datetime(2013,1,1)
end = datetime.datetime(2018,1,1)

tesla = web.DataReader("TSLA", 'iex', start, end)
ford = web.DataReader('F','iex', start, end)
gm = web.DataReader('GM', 'iex', start, end)

# 1 Daily Percentage Change

tesla['returns'] = (tesla['close']/tesla['close'].shift(1)) -1
# print('tesla.head()\n', tesla.head())

tesla['returns'] = tesla['close'].pct_change(1)
# print('tesla.head()\n', tesla.head())

ford['returns'] = ford['close'].pct_change(1)
gm['returns'] = gm['close'].pct_change(1)

print('ford.head()\n', ford.head())
print('gm.head()\n', gm.head())

ford['returns'].hist(bins=50)
plt.show()

gm['returnss'].hist(bins=50)
plt.show()

tesla['returns'].hist(bins=50)
plt.show()

# Histogram
tesla['returns'].hist(bins=100, label='Tesla', figsize=(10,8), alpha=0.5)
gm['returns'].hist(bins=100, label='GM', alpha=0.5)
ford['returns'].hist(bins=100, label='Ford', alpha=0.5)
plt.legend()
plt.show()

# KDE
tesla['returns'].plot(kind='kde', label='Tesla', figsize=(12,6))
gm['returns'].plot(kind='kde', label='GM')
ford['returns'].plot(kind='kde', label='Ford')
plt.legend()
plt.show()

# Box plot
box_df = pd.concat([tesla['returns'], gm['returns'], ford['returns']], axis=1)
box_df.columns = ['Tesla Returns', 'GM Returns', 'Ford Returns']
box_df.plot(kind='box', figsize=(8,11), colormap='jet')
plt.show()

# Comparing Daily Returns between stocks

pd.plotting.scatter_matrix(box_df, figsize=(8,8), alpha=0.2, hist_kwds={'bins':50})
plt.show()

# 2 Cumulative Daily Returns

tesla['Cumulative Return'] = (1 + tesla['returns']).cumprod()
ford['Cumulative Return'] = (1+ ford['returns']).cumprod()
gm['Cumulative Return'] = (1 + gm['returns']).cumprod()

tesla['Cumulative Return'].plot(label='Tesla', figsize=(16, 8), title='Cumulative Return')
ford['Cumulative Return'].plot(label='Ford')
gm['Cumulative Return'].plot(label='GM')
plt.legend()
plt.show()

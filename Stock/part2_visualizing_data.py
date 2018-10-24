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

# 1
tesla['open'].plot(label='Tesla', figsize=(16, 8), title='Open Price')
gm['open'].plot(label='GM')
ford['open'].plot(label='Ford')
plt.legend()
plt.show()

# 2
tesla['volume'].plot(label='Tesla', figsize=(16,8), title='Volume Traded')
gm['volume'].plot(label='gm')
ford['volume'].plot(label='ford')
plt.legend()
plt.show()

print(ford['volume'].idxmax())

# What happened:
# http://money.cnn.com/2013/12/18/news/companies/ford-profit/
# https://www.usatoday.com/story/money/cars/2013/12/18/ford-2014-profit-warning/4110015/
# https://media.ford.com/content/dam/fordmedia/North%20America/US/2014/01/28/4QFinancials.pdf

# 3
tesla['Total Traded'] = tesla['open'] * tesla['volume']
ford['Total Traded'] = ford['open'] * ford['volume']
gm['Total Traded'] = gm['open'] * gm['volume']

tesla['Total Traded'].plot(label='Tesla', figsize=(16,8))
gm['Total Traded'].plot(label='GM')
ford['Total Traded'].plot(label='Ford')
plt.legend()
plt.ylabel('Total Traded')
plt.show()

print(tesla['Total Traded'].idxmax())

# What happened:
# http://money.cnn.com/2014/02/25/investing/tesla-record-high/
# https://blogs.wsj.com/moneybeat/2014/02/25/tesla-shares-surge-on-morgan-stanley-report/
# https://www.washingtonpost.com/news/wonk/wp/2014/02/25/teslas-stock-is-up-644-why-it-may-not-last/
# http://www.cnbc.com/2014/02/25/tesla-soars-ford-falls-in-consumer-reports-study.html


# 4 Plot out the MA50 and MA200 for GM.
gm['MA50'] = gm['open'].rolling(50).mean()
gm['MA200'] = gm['open'].rolling(200).mean()
gm[['open', 'MA50', 'MA200']].plot(label='gm', figsize=(16,8))
plt.show()


# 5 relationship by using scatter matrix plot
from pandas.plotting import scatter_matrix

car_comp = pd.concat([tesla['open'],gm['open'],ford['open']], axis=1)
car_comp.columns = ['Tesla Open', 'GM Open', 'Ford Open']

scatter_matrix(car_comp, figsize=(8,8), alpha=0.2, hist_kwds={'bins':50})
plt.show()

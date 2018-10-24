import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pandas_datareader
import datetime

import pandas_datareader.data as web

start = datetime.datetime(2013,1,1)
end = datetime.datetime(2018,1,1)
tesla = web.DataReader("TSLA", 'iex', start, end)

print('tesla \n',tesla.head())

# save to CSV
# tesla.to_csv('Tesla_Stock.csv')

# other car companies

ford = web.DataReader('F','iex', start, end)
gm = web.DataReader('GM', 'iex', start, end)

print('ford.head()\n', ford.head())

# ford.to_csv('Ford_Stock.csv')

print('gm.head()\n', gm.head())
# gm.to_csv('GM_Stock.csv')


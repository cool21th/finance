from pandas import read_csv
from matplotlib import pyplot

series = read_csv('monthly-car-sales.csv', header=0, index_col=0)

print(series.shape)
pyplot.plot(series)
pyplot.show()

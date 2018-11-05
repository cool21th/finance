from math import sqrt
from numpy import mean
from numpy import std
from pandas import DataFrame
from pandas import concat
from pandas import read_csv
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
from statistics import median

def train_test_split(data, n_test):
    return data[:-n_test], data[-n_test:]

def serires_to_supervised(data, n_in=1, n_out=1):
    df = DataFrame(data)
    cols = list()

    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))

    for i in range(0, n_out):
        cols.append(df.shift(-i))

    agg = concat(cols, axis=1)
    agg.dropna(inplace=True)
    return agg.value

def measure_rmse(actual, predicted):
    return sqrt(mean_squared_error(actual, predicted))

def difference(data, interval):
    return [data[i] - data[i -interval] for i in range(interval, len(data))]

def model_fit(train, config):
    return None

def model_predict(model, history, config):
    values = list()
    for offset in config:
        values.append(history[-offset])
    return median(values)

def walk_forward_validation(data, n_test, cfg):
    predictions = list()
    train, test = train_test_split(data, n_test)
    model = model_fit(train, cfg)

    history = [x for x in train]

    for i in range(len(test)):
        yhat = model_predict(model, history, cfg)
        predictions.append(yhat)
        history.append(test[i])

    error = measure_rmse(test, predictions)
    print('> %.3f' % error)
    return error

def repeat_evaluate(data, config, n_test, n_repeats=30):
    scores = [walk_forward_validation(data, n_test, config) for _ in range(n_repeats)]

    return scores

def summarize_scores(name, scores):
    scores_m, score_std = mean(scores), std(scores)
    print('%s: %.3f RMSE (+/- %.3f)' % (name, scores_m, score_std))
    pyplot.boxplot(scores)
    pyplot.show()

series = read_csv('monthly-car-sales.csv', header=0, index_col=0)
data = series.values

n_test = 12
config = [12, 24, 36]
scores = repeat_evaluate(data, config, n_test)
summarize_scores('persistence', scores)

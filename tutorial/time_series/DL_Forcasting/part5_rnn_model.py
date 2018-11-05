from math import sqrt
from numpy import array
from numpy import mean
from numpy import std
from pandas import DataFrame
from pandas import concat
from pandas import read_csv
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from matplotlib import pyplot


def train_test_split(data, n_test):
    return data[:-n_test], data[-n_test:]

def series_to_supervised(data, n_in=1, n_out=1):
    df = DataFrame(data)
    cols = list()
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
    for i in range(0, n_out):
        cols.append(df.shift(-i))

    agg = concat(cols, axis=1)

    agg.dropna(inplace=True)
    return agg.values

def measure_rmse(actual, predicted):
    return sqrt(mean_squared_error(actual, predicted))

def difference(data, interval):
    return [data[i] - data[i - interval] for i in range(interval, len(data))]

def model_fit(train, config):
    n_input, n_nodes, n_epochs, n_batch, n_diff = config
    if n_diff > 0:
        train = difference(train, n_diff)
    data = series_to_supervised(train, n_in=n_input)
    train_x, train_y = data[:, :-1], data[:, -1]
    train_x = train_x.reshape((train_x.shape[0], train_x.shape[1], 1))

    model = Sequential()
    model.add(LSTM(n_nodes, activation='relu', input_shape=(n_input,1)))
    model.add(Dense(n_nodes, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mse', optimizer='adam')

    model.fit(train_x, train_y, epochs=n_epochs, batch_size=n_batch, verbose=0)
    return model

def model_predict(model, history, config):
    n_input, _, _, _, n_diff = config
    correction = 0.0
    if n_diff > 0:
        correction = history[-n_diff]
        history = difference(history, n_diff)
    x_input = array(history[-n_input:]).reshape((1, n_input, 1))
    yhat = model.predict(x_input, verbose=0)
    return correction + yhat[0]


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
    print(' > %.3f' % error)
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

config = [36,50,100,100,12]
scores = repeat_evaluate(data, config, n_test)

summarize_scores('lstm', scores)

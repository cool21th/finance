## [How to Develop Deep Learning Models for Univariate Time Series Forecasting](https://machinelearningmastery.com/how-to-develop-deep-learning-models-for-univariate-time-series-forecasting/)

1. Problem Description
  
    The ‘monthly car sales‘ dataset summarizes the monthly car sales in Quebec, Canada between 1960 and 1968.
  
    dataset: [monthly-car-sales.csv](https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-car-sales.csv) 

    *part1_load_data.py*

2. Model Evaluation Test Harness

    Train-Test split : Train용 데이터와 Test용 데이터로 구분
    
    Series as Supervised Learning: 각각의 Sample들을 input, output으로 구분하며 NaN 데이터는 삭제진행
    
    Walk-Forward Validation
    Repeat Evaluation
    Summarize Performance

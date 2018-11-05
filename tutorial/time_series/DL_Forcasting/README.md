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
    
    *part2_model_evaluate.py*
    
3. Multilayer Perceptron Model

    간단한 feed-forward 모델
    
    loss Function은 mean squared error를 적용 하였음
    
    *part3_mlp_model.py*
    

4. Convolutional Neural Network Model

    Conv2D: Image data, Conv1D: sequences of text and time series
    
    CNN모델은 이미지 채널로 해석되는 각 time step의 여러 Feature들을 지원할 수 있음
    
    *part4_cnn_model.py*
    

5. Recurrent Neural Network Models

    시퀀스 데이터임에도 불구하고, LSTM 은 시계열 예측에서는 효과적이지 않음
    
    LSTM 변형
      
        CNN-LSTM : CNN Networks의 Features들을 LSTM input값
        ConvLSTM : LSTM unit의 input data를 CNN의 convolutional process를 이용
    
    *part5_rnn_model.py*
    
6. CNN LSTM

    *part6_cnn_rnn_model.py
    


## [Deep Learning in Characteristics-Sorted Factor models](https://arxiv.org/pdf/1805.01104.pdf)

### Abstract

To study the characteristics-sorted factor model in asset pricing, we develop a bottom-up approach with sota dl optimization.
With an economic objective to minimize pricing erros, we train a non-reduced-form neural network using firm characteristics [inputs], 
and generate factors [intermediate features], to fit security returns [outputs].
Sorting securities on firm characteristics provides a nonlinear activation to create long-short portfolio weights, as a hidden layer, from lag characteristics provides a nonlinear activation to create long-short portfolio weights, as a hidden layer, from lag characteristics to realized returns.
Our model offers an alternative perspective for dimension reduction on firm characteristics [inputs], rather than factor [intermediate features], and allows for both nonlinearity and interactions on inputs.
Our empirical findings are twofold.
We find robust statistical and economic evidence in out-of-sample portfolios and individual stock returns.
To interpret our deep factors, we show highly significant results in factor investing via the squared Sharpe ratio test, as well as improvement in dissecting anomalies.

### Introduction

Asset pricing models study why different expected returns.
According to ICAPM of Metron, a combination of common factors captures the cross section of expected returns, and the regression intercept should be zero.
Therefore, the model fitness for asset pricing is not about the explained variation in time series, but the magnitude of intercepts, alphas, in the cross-section. 
This non-arbitrage restriction on alphas implies that simply adding factors leads to statistical overfitting (tiem series R^2) but does not caus economical overfitting (intercepts).

In empirical asset pricing studies, researchers typically sort securities on firm characteristics and create long-short portfolios as common risk factors to build asset pricing models. 
For example, the Nobel prize research of Fama and French add SMB  and HML to CAPM.
However, almost all proposed factor models have rejected the zero-alpha hypothesis.
We want to approach this puzzle, with a machine learning perspective, as an optimization problem: How does one construct a factor model to minimize priocing errors or alphas?

A rising literature 

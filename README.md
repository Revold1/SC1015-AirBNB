# SC1015-AirBNB

### Problem definition 
Predict the price of AirBNB, then determine whether it is over/underprice. 
Dataset: London Weekday from [Airbnb Price Determinants in Europe]("https://www.kaggle.com/datasets/thedevastator/airbnb-price-determinants-in-europe")


### Todos
1) EDA (To choose important features is important)  
  a) Features we are using  (Total 7 features)
      Categorical: room_type, biz,  
      Numerical: person_capacity, bedrooms, dist, attr_index_norm, rest_index_norm
* To do: Add in justifications for the categorical/ numerical data we chose 

Our Model Used (Ensemble methods)
Ensemble learning is a machine learning paradigm where multiple models (often called “weak learners”) are trained to solve the same problem and combined to get better results. The main hypothesis is that when weak models are correctly combined we can obtain more accurate and/or robust models.
https://towardsdatascience.com/ensemble-methods-bagging-boosting-and-stacking-c9214a10a205 


2) Choosing a [model]("https://scikit-learn.org/stable/modules/ensemble.html") to predict the price.  
  a) Forests of Randomized Tree (Jonathan)  
      https://www.geeksforgeeks.org/random-forest-regression-in-python/
      Every decision tree has high variance, but when we combine all of them together in parallel then the resultant variance is low as each decision tree gets perfectly trained on that particular sample data, and hence the output doesn’t depend on one decision tree but on multiple decision trees. In the case of a classification problem, the final output is taken by using the majority voting classifier. In the case of a regression problem, the final output is the mean of all the outputs. Random Forest is an ensemble technique capable of performing both regression and classification tasks with the use of multiple decision trees and a technique called Bootstrap and Aggregation, commonly known as bagging. The basic idea behind this is to combine multiple decision trees in determining the final output rather than relying on individual decision trees. 
  b) AdaBoost (Wei Siong)  
  AdaBoost algorithm, short for Adaptive Boosting, is a Boosting technique used as an Ensemble Method in Machine Learning. It is called Adaptive Boosting as the weights are re-assigned to each instance, with higher weights assigned to incorrectly classified instances. Boosting is used to reduce bias as well as variance for supervised learning. It works on the principle of learners growing sequentially. Except for the first, each subsequent learner is grown from previously grown learners. In simple words, weak learners are converted into strong ones. The AdaBoost algorithm works on the same principle as boosting with a slight difference. 
  c) Histogram-Based Gradient Boost (Kieran)  
  Gradient boosting is a generalization of boosting algorithms like AdaBoost to a statistical framework that treats the training process as an additive model and allows arbitrary loss functions to be used, greatly improving the capability of the technique. As such, gradient boosting ensembles are the go-to technique for most structured (e.g. tabular data) predictive modeling tasks.

### Key takeways from our primary EDA


## General Guidelines to fulfill 

Prerequisites: Dataset Selection

    What dataset will you be working on? One good source of datasets is https://www.kaggle.com/datasets where you may find interesting projects to work on
    Try to find interesting datasets where you can formulate meaningful tasks
    Try to find tabular/structured datasets instead of images(CV) or text(NLP).

Checkpoint 1. Introduction

    Detailed introduction to your project objective, e.g. what problem you are going to solve based on what dataset.

    Briefly review the significance of your topic, e.g. any potential applications of your project.

    Summarize the organization of your report, e.g. in Section xx we do xx.

Checkpoint 2. Data Preprocessing

    Detailed description on your dataset via statistics and visualization.

    Detailed statements on why and how you perform data preprocessing, e.g. data cleaning, normalization, transformation, data augmentation.

Checkpoint 3. Methodology

    Explain the reason for choosing your machine learning model.
    
    We needed to choose a regression model to predict the price of the airbnb (response) based on the variables of where the airbnb is located/type of airbnb (predictors). After prediction of prices, we can see if the airbnb is overprice/underprice, i.e if predicted > realsum the airbnb is underpriced. 

    Detailed & formal introduction to your model. You must provide the formulation or diagram of the model you use thoroughly. Clarify the input and output of your model.
    
      a) Forests of Randomized Tree (Jonathan)  
      https://www.geeksforgeeks.org/random-forest-regression-in-python/
      Every decision tree has high variance, but when we combine all of them together in parallel then the resultant variance is low as each decision tree gets perfectly trained on that particular sample data, and hence the output doesn’t depend on one decision tree but on multiple decision trees. In the case of a classification problem, the final output is taken by using the majority voting classifier. In the case of a regression problem, the final output is the mean of all the outputs. Random Forest is an ensemble technique capable of performing both regression and classification tasks with the use of multiple decision trees and a technique called Bootstrap and Aggregation, commonly known as bagging. The basic idea behind this is to combine multiple decision trees in determining the final output rather than relying on individual decision trees. 
      b) AdaBoost (Wei Siong)  
      AdaBoost algorithm, short for Adaptive Boosting, is a Boosting technique used as an Ensemble Method in Machine Learning. It is called Adaptive Boosting as the weights are re-assigned to each instance, with higher weights assigned to incorrectly classified instances. Boosting is used to reduce bias as well as variance for supervised learning. It works on the principle of learners growing sequentially. Except for the first, each subsequent learner is grown from previously grown learners. In simple words, weak learners are converted into strong ones. The AdaBoost algorithm works on the same principle as boosting with a slight difference. 
      c) Histogram-Based Gradient Boost (Kieran)  
      Gradient boosting is a generalization of boosting algorithms like AdaBoost to a statistical framework that treats the training process as an additive model and allows arbitrary loss functions to be used, greatly improving the capability of the technique. As such, gradient boosting ensembles are the go-to technique for most structured (e.g. tabular data) predictive modeling tasks.

    Clarify how you train and inference based on the model you choose.
    
    Describe the training methods/ train test split.

    Clarify the choice of hyperparameters of your model.
    
    We chose the best model out of the 3 listed, based on 2 variables R^2 and MSE. The best model for prediction is HistGradientBoostingRegressor model, its has the highest R^2 value and the lowest MSE. After choosing this model, we apply gridsearch to find the best hyperparameter of the model. 
    
    Hyperparameters that we are looking out for: 
    
Checkpoint 4. Experiments

    Detailed introduction to the performance metrics you use for experiments.
    
    -> We use 2 metrics to evaluate the accuracy of our model
    1) Explained Variance(R^2): 0 <= R^2 <= 1. 1 being the best, 0 being the worst. 

    Briefly introduce which baselines you are comparing with, e.g. you compare your model against a random guessing, a decision tree, a linear model, etc. This part is compulsory.

    Detailed model selection and comparison: Is your model fitting well compared to your baselines? Discuss about underfitting/overfitting if any. Important
    
    Which configuration (hyperparameter choices) performs the best? What numerical results lead to these conclusions? Your conclusion is held in what sense? The analysis of this part (not the performance alone) is the most important.
    How we use our prediction to prove our hypothesis.

Checkpoint 5. Conclusion

    Briefly summarize your findings in Experiments.

    The limitation of your current model. How you can improve your model.





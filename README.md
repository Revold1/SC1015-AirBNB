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

2) Choosing a [model]("https://scikit-learn.org/stable/modules/ensemble.html") to predict the price.  
  a) Forests of Randomized Tree (Jonathan)  
  b) AdaBoost (Wei Siong)  
  c) Histogram-Based Gradient Boost (Kieran)  
  
3) Verifying whether the model is accurate, use guest satisfaction rating.  
  a) Separate Train-Test set  
  b) Use train set to train the model  
  c) Predict the prices for test set  
  d) Get the difference between the realsum of train and test  
  e) Verify it with guest satisfaction rating with one of the following methods:  
    i) Do linear regression, and observe how skew is the graph  
    ii) Put the data into two categories: Underprice and Overprice. For each category, find the mean guest satisfaction rating. Ideally, the value for Underprice category should be higher than the value for Overprice category.  

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

    Detailed & formal introduction to your model. You must provide the formulation or diagram of the model you use thoroughly. Clarify the input and output of your model.

    Clarify how you train and inference based on the model you choose.

    Clarify the choice of hyperparameters of your model.

Checkpoint 4. Experiments

    Detailed introduction to the performance metrics you use for experiments.

    Briefly introduce which baselines you are comparing with, e.g. you compare your model against a random guessing, a decision tree, a linear model, etc. This part is compulsory.

    Detailed model selection and comparison: Is your model fitting well compared to your baselines? Discuss about underfitting/overfitting if any. Important

    Which configuration (hyperparameter choices) performs the best? What numerical results lead to these conclusions? Your conclusion is held in what sense? The analysis of this part (not the performance alone) is the most important.

Checkpoint 5. Conclusion

    Briefly summarize your findings in Experiments.

    The limitation of your current model. How you can improve your model.





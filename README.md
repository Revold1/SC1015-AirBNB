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




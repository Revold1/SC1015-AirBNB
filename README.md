# Welcome to AirBNB Price Checker

## About
Choosing accomodation on-the-go is often a headache for travellers. Travellers on a tight budget like students need to quickly find the most value for money AirBnB, while not spending too much time researching.

Dataset on Kaggle: Airbnb Price Determinants in Europe <https://www.kaggle.com/datasets/thedevastator/airbnb-price-determinants-in-europe>

For detailed walkthrough, please view the source code in order from:

1. [Exploratory Data Analysis](https://github.com/Revold1/SC1015-AirBNB/blob/main/EDA.ipynb)
2. [Adaptive Boost Model](https://github.com/Revold1/SC1015-AirBNB/blob/main/AdaBoost%20Regression%20Model.ipynb)
3. [Forest Of Randomized Trees](https://github.com/Revold1/SC1015-AirBNB/blob/main/ForestofRandomisedTrees.ipynb)
4. [Histogram Gradient Boosting Model](https://github.com/Revold1/SC1015-AirBNB/blob/main/histgradboosting.ipynb)

[Helper Functions] (https://github.com/Revold1/SC1015-AirBNB/blob/main/helper_functions.py)  
  
## Contributors

- ZiLong : EDA & Forest of Randomized Trees
- Wei Siong : AdaBoost and Hyperparameter tuning
- Kieran : Histogram Gradient Boost Model and conclusion 

## Problem Definition

- Hypothesis: Listing that are more expensive are less likely to be of good value

## Models Used

1. Forest of Randomized Trees 
2. Adaptive Boosting
3. Histogram Based Gradient Boosting

|                          | Random Forest | AdaBoost | HistGradBoost | HistGradBoost (After Tuning) |
|--------------------------|---------------|----------|---------------|------------------------------|
| Explained Variance (R^2) | 0.69615       | 0.44313  | 0.70618       | 0.71781                      |
| Mean Square Error (MSE)  | 8882          | 15065    | 8109          | 7788                         |


## Conclusion

- As prices increases, percentage of AirBNB's that are underpriced decreases (Agree with our hypothesis)
- Budget AirBNB are of execellent value 
- Overpaying becomes less of a concern as price increases 
- Sellers should appropriately set their AirBNB prices with respect to its price category

## What did we learn from this project?

- What is ensemble models : Bagging vs Boosting
- 3 new models: Adaboost, ForestofRandomizedTrees, HistGradBoost 
- Troubleshooting the adaboost model 
- Tuning of hyperparameters/ GridSearch 
- 

## References

- <https://www.geeksforgeeks.org/random-forest-regression-in-python>
- <https://seaborn.pydata.org/generated/seaborn.pairplot.html>
- <https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python>
- <https://towardsdatascience.com/ensemble-methods-bagging-boosting-and-stacking-c9214a10a205>
- <https://www.analyticsvidhya.com/blog/2021/09/adaboost-algorithm-a-complete-guide-for-beginners>
- <https://machinelearningmastery.com/adaboost-ensemble-in-python>
- <https://www.analyticsvidhya.com/blog/2021/09/adaboost-algorithm-a-complete-guide-for-beginners/>
- <https://machinelearningmastery.com/adaboost-ensemble-in-python/>
- <https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python/>

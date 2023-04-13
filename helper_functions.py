import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error


def clean_data(df):
    #return dataframe
    #remove NULL Columns from dataframe 
    df = df.drop(columns=['Unnamed: 0']) 

    #remove outliers 'realSum' from dataframe 
    Q1 = df['realSum'].quantile(0.25)
    Q3 = df['realSum'].quantile(0.75)
    df = df.loc[(( df['realSum'] > (Q1 - 1.5 * (Q3 - Q1))) & ( df['realSum'] < (Q3 + 1.5 * (Q3 - Q1))))]

    #Apply categorical label to columns 
    df[['room_type', 'room_shared', 'room_private', 'host_is_superhost', 'multi', 'biz']].apply(lambda x: x.astype('category'))

    #Convert Roomtype to oridinal 
    df["room_type"] =  df["room_type"].replace({'Shared room': 0, 'Private room': 1, 'Entire home/apt': 2})
    
    return df 

def model_statistics(model, x_test, y_test, y_test_pred):
    # Check the Goodness of Fit (on Test Data)
    print("Goodness of Fit of Model \tTest Dataset")
    print("Explained Variance (R^2) \t:", model.score(x_test, y_test))
    print("Mean Squared Error (MSE) \t:", mean_squared_error(y_test, y_test_pred))
    print() 

def plot_pred(y_test, y_test_pred):
   # Plot the Predictions vs the True values
    f, axes = plt.subplots(1, 1, figsize=(24, 12))
    axes.scatter(y_test, y_test_pred, color = "green")
    axes.plot(y_test, y_test, 'w-', linewidth = 3, color="red")
    axes.set_xlabel("True values of the Response Variable (Test)")
    axes.set_ylabel("Predicted values of the Response Variable (Test)")
    plt.show() 

def extract_r_p(df):
    y = pd.DataFrame(df["realSum"])
    x = pd.DataFrame(df[["person_capacity", "bedrooms", "dist", "attr_index_norm", "rest_index_norm", "room_type", "biz"]])

    return x, y
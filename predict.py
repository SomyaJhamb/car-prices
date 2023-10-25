# Importing the necessary Python modules.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import plot_confusion_matrix, r2_score, mean_absolute_error, mean_squared_error, mean_squared_log_error


# ML classifier Python modules
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression

@st.cache()
def prediction(car_df,carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick):
  x = car_df.iloc[:,:-1]
  y = car_df["price"]
  X_train, X_test, y_train, y_test = train_test_split(x,y,test_size = 0.3,random_state =42)
  lr = LinearRegression()
  lr.fit(X_train,y_train)
  score = lr.score(X_train,y_train)
  price = lr.predict([[carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick]])
  price = price[0]



  y_test_pred = lr.predict(X_test)
  test_r2_score = r2_score(y_test,y_test_pred)
  test_mae = mean_absolute_error(y_test,y_test_pred)
  test_msle = mean_squared_log_error(y_test,y_test_pred)
  test_rmse = np.sqrt(mean_squared_error(y_test,y_test_pred))
  return price, score, test_r2_score, test_mae, test_msle, test_rmse

def app(car_df):
  # Add 9 slider widgets for accepting user input for 9 features.
  st.markdown("<body><h1 style='color:black;font-size:40px'> <center> <b> PREDICT </b></center></h1></body>",unsafe_allow_html = True)

  st.markdown("""
        <h2 style = "color: purple;font-size :23px"><b>Select your values</b></h2>
    """,unsafe_allow_html = True)

  carwidth = st.slider("Input carwidth", float(car_df['carwidth'].min()), float(car_df['carwidth'].max()))
  enginesize = st.slider("Input enginesize", float(car_df['enginesize'].min()), float(car_df['enginesize'].max()))
  horsepower = st.slider("Input horsepower", float(car_df['horsepower'].min()), float(car_df['horsepower'].max()))

  drivewheel_fwd = st.radio("IS IT A FWD DRIVE WHEEL CAR",("Yes","No"))
  if drivewheel_fwd == "No":
    drivewheel_fwd = 0
  else:
    drivewheel_fwd = 1

  car_company_buick = st.radio("IS IT MANUFACTURED BY BUICK?",("YES","NO"))
  if car_company_buick == "No":
    car_company_buick = 0
  else:
    car_company_buick = 1
  
  if st.button("Predict"):
    st.subheader("PREDICTION RESULTS")
    price, score, car_r2, car_mae, car_msle, car_rmse = prediction(car_df,carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick)
    st.success(f"Predicted price of the car is {price}")
    st.info(f"Accuracy score is {score}" )
    st.info(f"R2 score is {car_r2}")
    st.info(f"MAE is {car_mae}" )
    st.info(f"MSLE is {car_msle} ")
    st.info(f"RMSE is {car_rmse}" )

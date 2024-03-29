# Importing the necessary Python modules.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import plot_confusion_matrix

# ML classifier Python modules
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def app(car_df):
  st.markdown("<body><h1 style='color:black;font-size:40px'> <center> <b> VISUALISE DATA </b></center></h1></body>",unsafe_allow_html = True)
  # Write your code to filter streamlit warnings 
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.markdown("""
        <h2 style = "color: purple;font-size :23px"><b>Scatter Plot</b></h2>
    """,unsafe_allow_html = True)


  # Choosing x-axis values for scatter plots.
  features_list = st.multiselect("Select the x-axis values:",
                                  ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))

  # Create scatter plots.
  for feature in features_list:
    st.subheader(f"Scatter plot between {feature} and GlassType")
    plt.figure(figsize = (12, 6))
    sns.scatterplot(x = feature, y = 'price', data = car_df)
    st.pyplot()
  
  st.markdown("""
        <h2 style = "color: purple;font-size :23px"><b>Visualisation Selecter</b></h2>
    """,unsafe_allow_html = True)

  # Add a multiselect in the sidebar with label 'Select the charts or plots:'
  # and pass the remaining 6 plot types as a tuple i.e. ('Histogram', 'Box Plot', 'Count Plot', 'Pie Chart', 'Correlation Heatmap', 'Pair Plot').
  # Store the current value of this widget in a variable 'plot_types'.
  plot_types = st.multiselect("Select the charts or plots:",
                                      ('Histogram', 'Box Plot','Correlation Heatmap'))


  # Display box plot using the 'matplotlib.pyplot' module and the 'st.pyplot()' function.
  if 'Histogram' in plot_types:
    st.subheader("Histogram")
    columns = st.selectbox("Select the column to create its histogram",
                                  ('carwidth', 'enginesize', 'horsepower'))
    # Note: Histogram is generally created for continous values not for discrete values.
    plt.figure(figsize = (12, 6))
    plt.title(f"Histogram for {columns}")
    plt.hist(car_df[columns], bins = 'sturges', edgecolor = 'black')
    st.pyplot()

  # Create box plot using the 'seaborn' module and the 'st.pyplot()' function.
  if 'Box Plot' in plot_types:
    st.subheader("Box Plot")
    columns = st.selectbox("Select the column to create its box plot",
                                  ('carwidth', 'enginesize', 'horsepower'))        
    plt.figure(figsize = (12, 2))
    plt.title(f"Box plot for {columns}")
    sns.boxplot(car_df[columns])
    st.pyplot()

  # Display correlation heatmap using the 'seaborn' module and the 'st.pyplot()' function.
  if 'Correlation Heatmap' in plot_types:
    st.subheader("Correlation Heatmap")
    plt.figure(figsize = (10, 6))
    ax = sns.heatmap(car_df.corr(), annot = True) # Creating an object of seaborn axis and storing it in 'ax' variable
    bottom, top = ax.get_ylim() # Getting the top and bottom margin limits.
    ax.set_ylim(bottom + 0.5, top - 0.5) # Increasing the bottom and decreasing the bottom margins respectively.
    st.pyplot()



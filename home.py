# S5.1: Configure the home as directed above.
import streamlit as st
def app():
  import turtle
  st.markdown("<body><h1 style='color:black;font-size:40px'> <center> <b> CAR PRICE PREDICTION APP </b></center></h1></body>",unsafe_allow_html = True)
  st.markdown("<h2 style = 'color:brown;font-size:30px'><i>About app</i></h2><p style='color:darkslategrey;font-size:25px'><center>The <b>CAR PRICE PREDICTION APP</b> is a  web app that allows a user to predict the prices of a car based on their engine size, horse power, dimensions and the drive wheel type parameters. In addition, the user can visualise the dataset and its attributes, plot different graphs for the dataset used for machine learning purposes.</center> </p>", unsafe_allow_html = True)
  st.markdown("""
  	<h2 style = "color: green;font-size :25px"> You can navigate to: </h2>
  	<h2 style = "color: purple;font-size :23px"><b>1) View Data</b></h2>
  	<p> This part of the web app allows the user to view complete raw dataset, analytical summary of the dataset, names of all the columns in dataset, data type of each column and the column data upon selecting from drop down menu.</p>
  	<h2 style = "color: purple;font-size :23px"><b>2) Visualise Data</b></h2>
  	<p> A user can visualise the data by boxplots, histograms and scatter plots with the selected features. A correlation heatmap for the dataset can also be created. </p>
  	<h2 style = "color: purple;font-size :23px"><b>3) Predict</b></h2>
  	<p> The user needs to define the type of car by telling the values for all the prompted parameters. Based on the submitted parameters, the price of the car is predicted. Along with the predicted price, the accuracy, r2score, Mean absolute error, Mean squared log error and mean squared error of the prediction are displayed. </p>
  	""",unsafe_allow_html = True)

  
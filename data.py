# S6.1: Design the View Data page of the multipage app.
# Import necessary modules
import streamlit as st
import pandas as pd
import numpy as np
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.markdown("<body><h1 style='color:black;font-size:40px'> <center> <b> VIEW DATA</b></center></h1></body>",unsafe_allow_html = True)

  with st.beta_expander("View Dataset"):
  	st.table(car_df)
  
  st.markdown("""
        <h2 style = "color: purple;font-size :23px"><b>Columns Description</b></h2>
    """,unsafe_allow_html = True)

  if st.checkbox("Show summary"):
    st.table(car_df.describe())

  beta_col1, beta_col2, beta_col3 = st.beta_columns(3)

  # Add a checkbox in the first column. Display the column names of 'car_df' on the click of checkbox.
  with beta_col1:
    if st.checkbox("Show all column names"):
        st.table(list(car_df.columns))

  # Add a checkbox in the second column. Display the column data-types of 'car_df' on the click of checkbox.
  with beta_col2:
  	if st.checkbox("View column data-type"):
  		st.table(car_df.dtypes)

  # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
  with beta_col3:
  	if st.checkbox("View column data"):
  		column_data = st.selectbox('Select column', tuple(car_df.columns))
  		st.write(car_df[column_data])

import streamlit as st
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import plotly.express as px
import sklearn


st.set_page_config(layout="wide")
st.header("Student Dropout Analysis")
st.sidebar.title("Navigation")
data = pd.read_csv("data/dataset.csv")
if st.checkbox("Show Data"):
    st.write(data.head(100))

markdown=("""
      This application is used to basically analyses the core reasons of students taking 
          dropout in their phase of higher education. The dataset which  has been used is taken
          from UCI Machining repository.
""")
st.sidebar.info(markdown)

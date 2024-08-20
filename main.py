import pandas as pd
import streamlit as st
import seaborn as sns
import flagpy as fl
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

sources = ['https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021', 'https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature']

df = pd.read_csv('data\data_happiness_meantemperature.csv')

st.image('data\winter_vs_summer.jpg')

st.title('Is there a correlation between happiness and warm weather?')

st.text("""It's widely believed that people tend to be happier during the summer, 
while winter is often associated with sadness.
        
Let's explore the data from the 2021 World Happiness Report alongside the average annual
temperatures of countries around the world to see what insights we can uncover.\n""")

st.dataframe(df)
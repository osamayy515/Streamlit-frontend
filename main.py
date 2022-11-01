import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Welcome To My Data Science Project!')
    st.text('In this project I look the transactions of taxi in NYC. ...')

with dataset:
    st.header('NYC taxi dataset')
    st.text('I found this dataset on https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page')

    taxi_data = pd.read_csv('data/taxi_data.csv')
    st.write(taxi_data.head())

    st.subheader('Pick-up location ID distribution on the NYC dataset')
    pulocation_dist = pd.DataFrame(taxi_data['PULocationID'].value_counts()).head(50)
    st.bar_chart(pulocation_dist)

with features:
    st.header('The features I created')


with model_training:
    st.header('Time to train the model!')
    st.text('Here you get to choose the hyperparameters of the model and see how the performance changes!')


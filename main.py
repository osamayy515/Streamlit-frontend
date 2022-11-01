import streamlit as st

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

with features:
    st.header('The features I created')


with model_training:
    st.header('Time to train the model!')
    st.text('Here you get to choose the hyperparameters of the model and see how the performance changes!')

import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Welcome To My Data Science Project!')
    st.text('In this project I look the transactions of taxi in NYC. ...')

st.cache(suppress_st_warning=True)
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

    st.markdown('* **First feature:** I created this feature because of this... I calculated it using this logic')
    st.markdown('* **Second feature:** I created this feature because of this... I calculated it using this logic')


with model_training:
    st.header('Time to train the model!')
    st.text('Here you get to choose the hyperparameters of the model and see how the performance changes!')

    sel_col, disp_col = st.columns(2)

    max_depth = sel_col.slider('What should be the max depth of the model?', min_value=10, max_value=100, value=20, step=10)

    n_estimators = sel_col.selectbox('How many tree should there be?', options=[100,200,300,'No limit'], index=0)

    input_feature = sel_col.text_input('Which feature should be used as the input feature?', 'PULocationID')
    
import streamlit as st
import pandas as pd

df = pd.read_csv('heart_failure.csv')

st.subheader('환자데이터')
st.dataframe(df.head())

st.metric(
    label='전체환자수',
    value=f'{len(df)}명',
    delta='29건 수집'
)
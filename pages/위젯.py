import streamlit as st
import pandas as pd

df = pd.read_csv('heart_failure.csv')

age_max = st.slider(
    '최대 나이', 40, 95, 70)

filtered = df[df['age']<= age_max]
st.write(f'{len(filtered)}명이 조건에 해당해요..')
st.dataframe(filtered)
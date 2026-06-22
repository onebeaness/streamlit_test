import streamlit as st
import pandas as pd

df = pd.read_csv('heart_failure.csv')

choice = st.selectbox(
    '성별', ['남성','여성']
)
code = 1 if choice == '남성' else 0
result = df[df['sex'] == code ]
st.write(f'{len(result)}명')
st.dataframe(result)
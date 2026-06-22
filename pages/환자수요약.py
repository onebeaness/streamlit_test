import streamlit as st
import pandas as pd

df = pd.read_csv('heart_failure.csv')
st.title("심부전 환자 데이터")
st.dataframe(df.head(10))

avg = df['age'].mean()

st.metric('평균 나이',f'{avg:.1f}세')
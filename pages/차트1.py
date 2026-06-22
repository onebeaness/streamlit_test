

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('heart_failure.csv')

fig,ax = plt.subplots()

ax.hist(df['age'],bins=20,color=
        '#5bafb8')
ax.set_xlabel('나이')
ax.set_ylabel('환자 수')

st.pyplot(fig)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('heart_failure.csv')

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

counts = df['DEATH_EVENT'].value_counts()

# st.bar_chart(counts)

fig,ax=plt.subplots()
ax.bar(['생존','사망'], counts, color=['blue','red'])
st.pyplot(fig)
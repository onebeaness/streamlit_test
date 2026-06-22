import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('heart_failure.csv')

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# st.columns()
# 화면을 좌우로 분할
# col1, col2 = st.columns(2)

# st.sidebar
# 왼쪽 고정 패널 (필터 영역)
# st.sidebar.slider(...)

# st.tabs()
# 탭으로 화면 전환
# t1, t2 = st.tabs([...])

st.sidebar.header('filter')
age=st.sidebar.slider('최대 나이',
                      40, 95, 70)
df=df[df['age']<=age]

c1,c2 = st.columns(2)
c1.metric('환자수', len(df))
c2.metric('평균 나이', f'{df.age.mean():.0f}')


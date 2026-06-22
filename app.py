
import streamlit as st, pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


st.title(" 심부전 분석")
st.write("👈 메뉴를 선택하세요")


st.title("📊 데이터")
df = pd.read_csv("heart_failure.csv")
st.dataframe(df)


# import streamlit as st
# def home():
#     st.title('홈')
# def data():
#     st.title('데이타')
    
# pg = st.navigation([
#     st.Page(home, title='홈',
#             icon="🏠", default=True),
# st.Page(data, title="데이터",
# icon="📊"),
# ])
# pg.run()

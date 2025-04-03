import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")

with st.sidebar:
    st.header("About app")
    st.write("this is item A")
st.header("This is a header")

st.markdown("This is a markdown")


col1, col2 = st.columns(2)


st.subheader("st.column")
with col1:
    x = st.slider("This is a slider", 1, 10)
with col2: 
    st.write("Hello World!")
    st.write(f"value is :red[x] is ", x)


st.subheader("area_chart")
chart_data = pd.DataFrame(np.random.randn(20 , 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

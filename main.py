import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400)
with col2:
    st.title("Lakshya Dhingra")
    content = """
    Hi, I am Lakshya! I am a student, majoring in Computer Science, learning Python. 
    I am studying at Barrett the Honors College, at Arizona State University.
    """
    st.info(content)

content2 = """
Below you can find some of the apps built by me in Python, feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])

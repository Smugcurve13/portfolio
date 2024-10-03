import streamlit as st



st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("https://avatars.githubusercontent.com/u/48555604?v=4")

with col2:
    st.title("Smugcurve13")
    my_desc = """
    Hi, I am Smugcurve13! I am a python programmer based out of India. I have recently learned how to make apps using python.
    I will be logging all of my current and finished projects in this portfolio website.
    More pages to come soon here. Stay Tuned!
    """
    st.info(my_desc)

content = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content)
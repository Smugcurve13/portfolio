import streamlit as st

st.header("Contact Us")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your Message")
    button = st.form_submit_button()
    if button:
        message = message + user_email
        st.info("Thanks for submitting")
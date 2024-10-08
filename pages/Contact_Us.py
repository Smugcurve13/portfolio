import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New Submisssion from {user_email}
From: {user_email}
{raw_message}
"""
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Thanks for submitting")
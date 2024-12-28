import streamlit as st
import send_email
 
st.title("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email address")
    raw_message = st.text_area("Enter your message")
    user_message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email.emailsend(user_message)
        st.info("The email was sent successfully")

# The email sending works locally but not on web server such as streamlit

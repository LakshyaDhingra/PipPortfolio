import streamlit as st

st.title("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email address")
    user_message = st.text_area("Enter your message")
    submit_button = st.form_submit_button("Submit")

import streamlit as st

def get_user_query():
    return st.text_input("Enter your research question:", key="initial_query")

def get_user_input():
    return st.text_input("Your response:", key="followup_query")

def render_chat(message):
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Assistant:** {message['content']}")

def show_progress(message: str):
    st.info(message)

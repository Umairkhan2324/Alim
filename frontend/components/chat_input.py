# frontend/components/chat_input.py
import streamlit as st

def chat_input_box():
    """
    Displays the chat input box and returns the user's prompt.
    """
    return st.chat_input("What would you like to research?") 
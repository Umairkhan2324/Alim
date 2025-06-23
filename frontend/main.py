# main.py
import streamlit as st
import sys
import os
import nest_asyncio

nest_asyncio.apply()

# Add project root to sys.path to resolve module not found errors
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from Agents.orchestrator.orchestrator_agent import run_orchestrator_sync, orchestrator
from components.chat_input import chat_input_box

# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="Alim - Your Research Assistant",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Alim - Your Research Assistant 📚")
st.caption("Alim is a research assistant powered by multiple AI agents.")

# --- Session State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Chat Interface ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := chat_input_box():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Alim is thinking..."):
            # Pass the entire conversation history to the orchestrator
            full_response = run_orchestrator_sync(orchestrator, st.session_state.messages)
            message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
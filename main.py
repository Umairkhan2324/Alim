# Simple Streamlit Chat Interface for Alim
import streamlit as st
import nest_asyncio
import json
import os
import sys

# --- Official Streamlit Path Fix ---
# Based on Streamlit's documentation and community best practices, this is the
# standard way to handle imports in a multi-file app deployed on the cloud.

# Check if we're on Streamlit Cloud. The path '/mount/src/alim' is specific to
# how Streamlit Cloud mounts the GitHub repository.
STREAMLIT_CLOUD_ROOT = '/mount/src/alim'

if os.path.exists(STREAMLIT_CLOUD_ROOT):
    # If we are on Streamlit Cloud, add its root to the path
    if STREAMLIT_CLOUD_ROOT not in sys.path:
        sys.path.insert(0, STREAMLIT_CLOUD_ROOT)
        print(f"Running on Streamlit Cloud. Added '{STREAMLIT_CLOUD_ROOT}' to sys.path.")
else:
    # If running locally, add the project's local root directory to the path
    LOCAL_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    if LOCAL_PROJECT_ROOT not in sys.path:
        sys.path.insert(0, LOCAL_PROJECT_ROOT)
        print(f"Running locally. Added '{LOCAL_PROJECT_ROOT}' to sys.path.")

# With the correct path set, this import should now work universally.
from Agents.orchestrator.orchestrator_agent import run_orchestrator_sync, orchestrator
from schemas.agent_schema import ResearchReport

# Apply nest_asyncio
nest_asyncio.apply()

# Streamlit config
st.set_page_config(page_title="Alim - Research Assistant", layout="wide", page_icon="📚")
st.title("Alim - Your Research Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help your research today?"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to research?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()

# If the last message is from the user, generate and display a new response
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    user_prompt = st.session_state.messages[-1]["content"]
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_orchestrator_sync(orchestrator, user_prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            # Rerun to display the new message immediately
            st.rerun()

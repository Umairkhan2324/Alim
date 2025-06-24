# main.py
import os
import sys
import json
import nest_asyncio
import streamlit as st

# Setup project root path before any local imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from Agents.orchestrator.orchestrator_agent import run_orchestrator_sync, orchestrator
from schemas import ResearchReport
from utils.logging_config import get_logger
from frontend.components.sidebar import setup_sidebar
from frontend.components.chat import display_messages

nest_asyncio.apply()
logger = get_logger(__name__)

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Alim - Research Assistant", layout="wide", page_icon="📚")
st.title("Alim")
setup_sidebar()

# --- Session State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help your research today?"}]

# --- Main Chat Interface ---
display_messages()

if prompt := st.chat_input("What would you like to research?"):
    logger.info(f"User entered prompt: {prompt}")
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()

# --- Process and Display Assistant Response ---
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    user_prompt = st.session_state.messages[-1]["content"]
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_orchestrator_sync(orchestrator, user_prompt)
            try:
                report_data = json.loads(response)
                report = ResearchReport(**report_data)
                st.session_state.messages.append({"role": "assistant", "report": report})
            except (json.JSONDecodeError, TypeError):
                st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
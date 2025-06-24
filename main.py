# Simple Streamlit Chat Interface for Alim
import streamlit as st
import nest_asyncio
import json

# Import the orchestrator from the root directory
from Agents.orchestrator.orchestrator_agent import run_orchestrator_sync, orchestrator
from schemas.agent_schema import ResearchReport

# Apply nest_asyncio
nest_asyncio.apply()

# Streamlit config
st.set_page_config(page_title="Alim - Research Assistant", layout="wide", page_icon="??")
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

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_orchestrator_sync(orchestrator, prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.markdown(response)
    st.rerun()

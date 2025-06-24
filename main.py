# Simple Streamlit Chat Interface for Alim
import streamlit as st
import nest_asyncio
import json
import os
import sys

# Robust path detection for Streamlit Cloud
# Check if we're on Streamlit Cloud and add the correct path
alim_path = '/mount/src/alim'
if os.path.exists(alim_path):
    # We're on Streamlit Cloud
    if alim_path not in sys.path:
        sys.path.insert(0, alim_path)
        print(f"Added {alim_path} to sys.path for Streamlit Cloud")
else:
    # Local development - use current directory
    current_dir = os.path.dirname(os.path.abspath(__file__)) if __file__ else os.getcwd()
    if current_dir and current_dir not in sys.path:
        sys.path.insert(0, current_dir)
        print(f"Added {current_dir} to sys.path for local development")

# Attempt to import orchestrator agent
try:
    from Agents.orchestrator.orchestrator_agent import run_orchestrator_sync, orchestrator
    print("Successfully imported orchestrator agent")
except ModuleNotFoundError as e:
    # Diagnostic output to Streamlit Cloud logs
    print("ImportError encountered:", e)
    print("sys.path =", sys.path)
    
    # Check what directories exist
    if os.path.exists('/mount/src/alim'):
        print("Contents of /mount/src/alim:", os.listdir('/mount/src/alim'))
        agents_path = '/mount/src/alim/Agents'
        if os.path.exists(agents_path):
            print("Contents of Agents directory:", os.listdir(agents_path))
            orchestrator_path = '/mount/src/alim/Agents/orchestrator'
            if os.path.exists(orchestrator_path):
                print("Contents of orchestrator directory:", os.listdir(orchestrator_path))
    
    # Fallback: dynamic import by file path
    import importlib.util
    orchestrator_file = '/mount/src/alim/Agents/orchestrator/orchestrator_agent.py'
    print("Looking for orchestrator at:", orchestrator_file)
    
    if os.path.exists(orchestrator_file):
        print("Orchestrator file found! Loading dynamically...")
        spec = importlib.util.spec_from_file_location("orchestrator_agent", orchestrator_file)
        module = importlib.util.module_from_spec(spec)
        sys.modules["orchestrator_agent"] = module
        spec.loader.exec_module(module)
        run_orchestrator_sync = module.run_orchestrator_sync
        orchestrator = module.orchestrator
        print("Successfully loaded orchestrator via fallback method")
    else:
        print("Orchestrator file not found at expected path")
        raise Exception("Could not load orchestrator agent")

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

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_orchestrator_sync(orchestrator, prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.markdown(response)
    st.rerun()

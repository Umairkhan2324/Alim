# Simple Streamlit Chat Interface for Alim
import streamlit as st
import nest_asyncio
import json
import os
import sys

# Fix the path to include the directory where this script is located
# Handle Streamlit Cloud's specific deployment structure
script_dir = os.path.dirname(os.path.abspath(__file__)) if __file__ else os.getcwd()

# For Streamlit Cloud, ensure we have the correct path to find Agents
if '/mount/src' in sys.path[0]:  # We're on Streamlit Cloud
    alim_path = '/mount/src/alim'
    if alim_path not in sys.path:
        sys.path.insert(0, alim_path)
        print(f"Added {alim_path} to sys.path for Streamlit Cloud")
else:  # Local development
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)

# Attempt to import orchestrator agent
try:
    from Agents.orchestrator.orchestrator_agent import run_orchestrator_sync, orchestrator
    print("Successfully imported orchestrator agent")
except ModuleNotFoundError as e:
    # Diagnostic output to Streamlit Cloud logs
    print("ImportError encountered: ", e)
    print("sys.path =", sys.path)
    print("Script directory:", script_dir)
    if script_dir and os.path.exists(script_dir):
        print("Script directory contents:", os.listdir(script_dir))
    
    # Check if we're on Streamlit Cloud and list the alim directory
    alim_path = '/mount/src/alim'
    if os.path.exists(alim_path):
        print(f"Contents of {alim_path}:", os.listdir(alim_path))
        agents_path = os.path.join(alim_path, 'Agents')
        if os.path.exists(agents_path):
            print(f"Contents of {agents_path}:", os.listdir(agents_path))
    
    # Fallback: dynamic import by file path
    import importlib.util, pathlib
    orchestrator_path = pathlib.Path(alim_path) / "Agents" / "orchestrator" / "orchestrator_agent.py"
    print("Looking for orchestrator at:", orchestrator_path)
    if orchestrator_path.exists():
        spec = importlib.util.spec_from_file_location("Agents.orchestrator.orchestrator_agent", orchestrator_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        run_orchestrator_sync = module.run_orchestrator_sync
        orchestrator = module.orchestrator
        print("Successfully loaded orchestrator via fallback method")
    else:
        print("Orchestrator file not found at expected path")
        raise

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

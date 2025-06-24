# Simple Streamlit Chat Interface for Alim
import streamlit as st
import nest_asyncio
import json
import os
import sys

# Fix the path to include the directory where this script is located
# This ensures that modules like 'Agents' and 'schemas' are discoverable.
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

# Attempt to import orchestrator agent
try:
    from Agents.orchestrator.orchestrator_agent import run_orchestrator_sync, orchestrator
except ModuleNotFoundError as e:
    # Diagnostic output to Streamlit Cloud logs
    print("ImportError encountered: ", e)
    print("sys.path =", sys.path)
    print("Script directory:", script_dir)
    if script_dir and os.path.exists(script_dir):
        print("Script directory contents:", os.listdir(script_dir))
    # Fallback: dynamic import by file path (works regardless of package resolution)
    import importlib.util, pathlib
    orchestrator_path = pathlib.Path(script_dir) / "Agents" / "orchestrator" / "orchestrator_agent.py"
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

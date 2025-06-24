# Simple Streamlit Chat Interface for Alim
import streamlit as st
import nest_asyncio
import json
import os
import sys

# Explicitly add the project root to sys.path for Streamlit Cloud deployment
# This ensures that modules like 'Agents' and 'schemas' are discoverable.
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Attempt to import orchestrator agent
try:
    from Agents.orchestrator.orchestrator_agent import run_orchestrator_sync, orchestrator
except ModuleNotFoundError as e:
    # Diagnostic output to Streamlit Cloud logs
    print("ImportError encountered: ", e)
    print("sys.path =", sys.path)
    print("Project root contents:", os.listdir(project_root))
    # Fallback: dynamic import by file path (works regardless of package resolution)
    import importlib.util, pathlib
    orchestrator_path = pathlib.Path(project_root) / "Agents" / "orchestrator" / "orchestrator_agent.py"
    if orchestrator_path.exists():
        spec = importlib.util.spec_from_file_location("Agents.orchestrator.orchestrator_agent", orchestrator_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        run_orchestrator_sync = module.run_orchestrator_sync
        orchestrator = module.orchestrator
    else:
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

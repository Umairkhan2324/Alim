import streamlit as st
from schemas import ResearchReport

def render_report(report: ResearchReport):
    """Displays a structured research report in Streamlit."""
    st.markdown(f"## {report.title}")
    
    with st.expander("Executive Summary", expanded=True):
        st.markdown(report.executive_summary)
        
    with st.expander("Key Findings"):
        for finding in report.key_findings:
            st.markdown(f"- {finding}")
            
    with st.expander("Detailed Analysis"):
        st.markdown(report.detailed_analysis, unsafe_allow_html=True)
        
    if report.sources:
        with st.expander("Sources"):
            for source in report.sources:
                st.markdown(f"- {source}")

def display_messages():
    """Displays the chat history."""
    for message in st.session_state.get("messages", []):
        with st.chat_message(message["role"]):
            if "report" in message:
                render_report(message["report"])
            else:
                st.markdown(message["content"])
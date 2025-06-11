import streamlit as st

def display_report(report_md: str):
    st.markdown("---")
    st.markdown("## Research Report")
    st.markdown(report_md)
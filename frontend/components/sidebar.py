import streamlit as st

def setup_sidebar():
    """Sets up the Streamlit sidebar with a new chat button."""
    with st.sidebar:
        st.header("Alim")
        st.caption("Your multi-agent research assistant.")
        
        if st.button("New Chat"):
            st.session_state.messages = []
            st.rerun()

        st.divider()
        st.markdown(
            "Built by [Umair Khan](https://github.com/Umairkhan2324) with multiple AI agents.",
            unsafe_allow_html=True,
        ) 
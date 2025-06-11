# main.py
import streamlit as st
from components.ui import get_user_query, get_user_input, render_chat
from components.progress import show_progress
from components.report_view import display_report
from Agents.orchestrator.orchestrator_agent import create_orchestrator_agent, run_orchestrator


def main():
    st.set_page_config(page_title="Multi-Agent Research Assistant", layout="wide")
    st.title("Multi-Agent Research Assistant")

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
        st.session_state["report"] = None

    # Step 1: Get initial query
    if not st.session_state["messages"]:
        query = ui.get_user_query()
        if query:
            st.session_state["messages"].append({"role": "user", "content": query})

    # Display conversation history
    for msg in st.session_state["messages"]:
        ui.render_chat(msg)

    # Create orchestrator
    orchestrator = create_orchestrator_agent()

    # Step 2: Clarification or research
    if st.session_state["messages"] and st.session_state["report"] is None:
        last = st.session_state["messages"][-1]
        # If assistant asked a question, get follow-up answer
        if last["role"] == "assistant" and last["content"].strip().endswith('?'):
            followup = ui.get_user_input()
            if followup:
                st.session_state["messages"].append({"role": "user", "content": followup})
        else:
            # Proceed to research
            with st.spinner("Research in progress..."):
                result = run_orchestrator(orchestrator, st.session_state["messages"])  # pass full history
                st.session_state["report"] = result
            progress.show_progress("Research completed!")

    # Step 3: Display final report
    if st.session_state["report"]:
        report_view.display_report(st.session_state["report"])


if __name__ == '__main__':
    main()
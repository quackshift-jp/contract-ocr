import streamlit as st


def next_file():
    if st.session_state["current_index"] < len(st.session_state["upload_files"]) - 1:
        st.session_state["current_index"] += 1


def previous_file():
    if st.session_state["current_index"] > 0:
        st.session_state["current_index"] -= 1

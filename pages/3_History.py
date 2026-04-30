import streamlit as st
import json
import os

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("Please login.")
    st.stop()

st.title("📁 My Analysis History")

user = st.session_state.get("username")
file_path = f"storage/history_{user}.json"

if os.path.exists(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    st.dataframe(data)
else:
    st.info("No history yet.")
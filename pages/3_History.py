import streamlit as st

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("Please login from the home page.")
    st.stop()
    
import streamlit as st

st.set_page_config(page_title="History", layout="wide")

st.title("📁 Analysis History")

st.info("History will be available in the premium version.")

st.markdown("""
Soon, users will be able to:

- Save uploaded files
- Save dashboard results
- Reopen previous analyses
- Export previous reports
- Compare historical performance
""")
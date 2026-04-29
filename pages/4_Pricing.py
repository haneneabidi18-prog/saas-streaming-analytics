import streamlit as st

if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.warning("Please login from the home page.")
    st.stop()
    
import streamlit as st

st.set_page_config(page_title="Pricing", layout="wide")

st.title("💎 Pricing")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Free")
    st.markdown("""
    **€0 / month**

    - Upload CSV
    - Basic dashboard
    - Limited analysis
    - No history
    """)

with col2:
    st.subheader("Pro")
    st.markdown("""
    **€29 / month**

    - User account
    - Saved history
    - Advanced dashboard
    - Export reports
    - Priority support
    """)
    st.button("Choose Pro")

with col3:
    st.subheader("Business")
    st.markdown("""
    **€199 / month**

    - Multi-user workspace
    - Live API
    - Custom dashboards
    - Telecom / OTT analytics
    - Premium support
    """)
    st.button("Contact Sales")
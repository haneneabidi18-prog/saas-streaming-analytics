import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title="Streaming Analytics SaaS",
    page_icon="📊",
    layout="wide"
)

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"]
)

authenticator.login(location="main")

name = st.session_state.get("name")
authentication_status = st.session_state.get("authentication_status")
username = st.session_state.get("username")

if authentication_status:
    authenticator.logout(location="sidebar")
    st.sidebar.success(f"Logged in as {name}")

    st.title("📊 Streaming Analytics SaaS")
    st.subheader("Premium analytics platform for OTT, media and telecom businesses")

    st.markdown("""
    Welcome to your premium SaaS dashboard.

    Use the sidebar to navigate:
    - About
    - Dashboard
    - History
    - Pricing
    """)

    st.info("Start by opening the Dashboard page from the sidebar.")

elif authentication_status is False:
    st.error("Username or password is incorrect")

elif authentication_status is None:
    st.warning("Please enter your username and password")